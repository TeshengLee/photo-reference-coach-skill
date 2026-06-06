#!/usr/bin/env python3
"""Extract useful photo metadata with graceful fallbacks."""

import json
import shutil
import subprocess
import sys
from pathlib import Path


FIELDS = {
    "FileType": "format",
    "MIMEType": "mime_type",
    "Make": "camera_make",
    "Model": "camera_model",
    "LensModel": "lens_model",
    "Lens": "lens",
    "FocalLength": "focal_length",
    "FocalLengthIn35mmFormat": "focal_length_35mm",
    "FNumber": "aperture",
    "ExposureTime": "shutter_speed",
    "ISO": "iso",
    "ExposureCompensation": "exposure_compensation",
    "WhiteBalance": "white_balance",
    "DateTimeOriginal": "captured_at",
    "ImageWidth": "width",
    "ImageHeight": "height",
    "GPSLatitude": "gps_latitude",
    "GPSLongitude": "gps_longitude",
    "GPSAltitude": "gps_altitude",
    "Software": "software",
}


def run_exiftool(path):
    if not shutil.which("exiftool"):
        return None
    proc = subprocess.run(
        ["exiftool", "-json", "-n", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode:
        return None
    records = json.loads(proc.stdout)
    return records[0] if records else None


def run_sips(path):
    if sys.platform != "darwin" or not shutil.which("sips"):
        return {}
    proc = subprocess.run(
        ["sips", "-g", "format", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    result = {}
    for line in proc.stdout.splitlines():
        if ":" not in line:
            continue
        key, value = (part.strip() for part in line.split(":", 1))
        if key == "format":
            result["format"] = value
        elif key == "pixelWidth":
            result["width"] = value
        elif key == "pixelHeight":
            result["height"] = value
    return result


def run_pillow(path):
    try:
        from PIL import ExifTags, Image
    except ImportError:
        return {}
    try:
        image = Image.open(path)
        result = {"format": image.format, "width": image.width, "height": image.height}
        exif = image.getexif()
        for tag_id, value in exif.items():
            name = ExifTags.TAGS.get(tag_id, str(tag_id))
            if name == "GPSInfo":
                gps = exif.get_ifd(tag_id)
                for gps_id, gps_value in gps.items():
                    gps_name = ExifTags.GPSTAGS.get(gps_id, str(gps_id))
                    if gps_name == "GPSLatitude":
                        result["gps_latitude"] = str(gps_value)
                    elif gps_name == "GPSLongitude":
                        result["gps_longitude"] = str(gps_value)
                    elif gps_name == "GPSAltitude":
                        result["gps_altitude"] = str(gps_value)
                continue
            mapped = FIELDS.get(name)
            if mapped:
                result[mapped] = str(value)
        return result
    except Exception:
        return {}


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: extract_image_metadata.py <image-path>")
    path = Path(sys.argv[1]).expanduser().resolve()
    if not path.is_file():
        raise SystemExit(f"File not found: {path}")

    source = "basic"
    raw = run_exiftool(path)
    if raw:
        data = {target: raw[key] for key, target in FIELDS.items() if key in raw}
        source = "exiftool"
    else:
        data = run_pillow(path)
        if data:
            source = "pillow"
        basic = run_sips(path)
        for key, value in basic.items():
            data.setdefault(key, value)

    meaningful = {
        "camera_make",
        "camera_model",
        "lens_model",
        "lens",
        "focal_length",
        "focal_length_35mm",
        "aperture",
        "shutter_speed",
        "iso",
        "exposure_compensation",
        "white_balance",
        "captured_at",
        "gps_latitude",
        "gps_longitude",
        "gps_altitude",
    }
    present = sorted(key for key in meaningful if data.get(key) not in (None, ""))
    gps_present = bool(data.get("gps_latitude") and data.get("gps_longitude"))
    device_present = bool(data.get("camera_make") or data.get("camera_model"))
    exposure_present = any(
        data.get(key)
        for key in ("focal_length", "focal_length_35mm", "aperture", "shutter_speed", "iso")
    )
    if device_present and exposure_present:
        status = "present"
    elif present:
        status = "partial"
    else:
        status = "stripped_or_unavailable"

    output = {
        "path": str(path),
        "metadata_status": status,
        "metadata_source": source,
        "gps_present": gps_present,
        "present_fields": present,
        "data": data,
        "interpretation": (
            "Use known metadata for device-specific advice."
            if status == "present"
            else "Use only the listed fields; do not infer missing device or capture details."
            if status == "partial"
            else "No embedded capture metadata found; continue with visual analysis."
        ),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2, default=str))


if __name__ == "__main__":
    main()
