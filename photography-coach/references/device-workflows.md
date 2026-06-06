# Phone vs Camera Workflows

Read this only when device-specific advice is needed.

## First Principle

Do not apply the same capture or editing recipe to phones and interchangeable-lens cameras.

- Phones rely heavily on computational processing, multi-frame HDR, sharpening, denoising, lens switching/cropping, and format choices such as HEIF/JPEG or ProRAW/DNG.
- Cameras give more direct control over focal length, physical aperture, shutter, ISO, sensor RAW, lens rendering, and depth of field.

## Phone Workflow

Check: exact model from metadata, selected camera/lens, HEIF/JPEG vs RAW/ProRAW, resolution, HDR/night/portrait mode, exposure compensation, and GPS.

Advise:
- Choose 1x for natural wide context, 2x/3x for cleaner geometry and compression; avoid 0.5x for people/interiors unless distortion is intentional.
- Lock focus/exposure when framing is stable. Reduce exposure when windows/skies clip.
- Prefer ProRAW/RAW when substantial white-balance, highlight, or color changes are expected. HEIF/JPEG is already processed; use gentler sharpening, clarity, denoise, and highlight recovery.
- Treat portrait blur as computational unless metadata/visual evidence indicates optical depth of field.
- Do not prescribe physical aperture changes when the phone has a fixed aperture; instead change lens, distance, subject-background separation, mode, or lighting.

## Interchangeable-Lens Camera Workflow

Check: make/model, sensor format, lens, real focal length and 35mm equivalent, aperture, shutter, ISO, stabilization, metering/exposure compensation, RAW/JPEG/HEIF, picture profile, and GPS.

Advise:
- Use focal length and camera distance to control perspective; use aperture and subject-background distance to control depth of field.
- Set shutter from subject motion and handholding risk, then aperture for depth, then ISO for exposure.
- RAW permits broader white-balance and tonal recovery; JPEG/HEIF already includes in-camera processing and needs gentler correction.
- Account for lens distortion, vignetting, chromatic aberration, sensor crop, stabilization, and diffraction where relevant.

## Format-Aware Editing

- Camera RAW / DNG / ProRAW: broader exposure, white-balance, highlight, and color latitude; start with profile and lens corrections.
- HEIF / JPEG: processed and compressed; avoid aggressive recovery, clarity, sharpening, and repeated exports.
- Screenshot / social download: treat as display-referred reference only. No reliable device, lens, EXIF, GPS, or original color-space conclusions.

## Sources

- Apple Support, Apple ProRAW: https://support.apple.com/119916
- Apple Support, location metadata: https://support.apple.com/guide/personal-safety/manage-location-metadata-in-photos-ips0d7a5df82/web
- Adobe, Camera Raw introduction: https://helpx.adobe.com/camera-raw/using/introduction-camera-raw.html
- Nikon, aperture and depth of field: https://www.nikonusa.com/learn-and-explore/c/tips-and-techniques/understanding-maximum-aperture
- Nikon, focal length: https://www.nikonusa.com/learn-and-explore/a/tips-and-techniques/understanding-focal-length.html
- Sony, RAW vs JPEG processing: https://www.sony.com/electronics/support/articles/00010263
