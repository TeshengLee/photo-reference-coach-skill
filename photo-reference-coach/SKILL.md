---
name: photo-reference-coach
description: Analyze reference photos as a photography coach. Use when the user shares or describes a photo and wants a full breakdown of why it works, including composition, subject placement, light, color, tone, editing style, Lightroom or Camera Raw adjustment direction, and concrete advice for shooting a similar sample in a similar scene. Also use when comparing a reference photo with the user's own photo to suggest how to shoot or edit closer to the reference.
---

# Photo Reference Coach

## Overview

Use this skill to turn a good photo into practical photography learning. Explain both the visual taste and the repeatable method: why the reference looks good, how the image was likely made, and how the user can shoot or edit toward a similar result.

Default to Chinese when the user writes in Chinese. Be concrete, visually observant, and honest about uncertainty. Do not pretend to know the original camera settings or editing parameters unless they are visible in metadata or provided by the user.

## Mode Selection

Choose the mode from the user's intent:

- **Reference analysis**: The user wants to understand one image. Focus on appreciation, composition, light, color, tone, and likely editing logic.
- **Shoot-like-this plan**: The user wants to make a similar sample. Turn the reference into a scene plan: location, time, light, camera position, focal length, subject arrangement, exposure priorities, and editing path.
- **Reference match**: The user provides a reference plus their own image. Compare the two and give prioritized shooting and editing steps to move the user's image closer to the reference.
- **Pre-shoot planning**: The user describes a scene, outfit, place, weather, gear, or desired style. Give a practical plan even if no image is attached.

If an image is expected but unavailable, ask for the image. If the user gives enough description to proceed, provide a provisional plan and state which parts should be checked after seeing the image.

## Image Reading Workflow

When an image is available, inspect it before giving advice. Cover these dimensions in order:

1. **First impression**: State the image's mood, genre, and main viewing anchor in 2-4 sentences.
2. **Subject and story**: Identify what the viewer notices first, what supports it, and what should stay quiet.
3. **Composition**: Discuss framing, crop ratio, subject position, lines, shapes, symmetry/asymmetry, layers, foreground/background, depth, negative space, edge control, and visual weight.
4. **Light**: Infer light direction, softness, contrast, time of day, weather, fill, backlight, window light, mixed light, and shadow quality.
5. **Color**: Identify dominant colors, accent colors, warm/cool balance, saturation strategy, skin or object color treatment, and color harmony.
6. **Tone**: Discuss black point, white point, highlight roll-off, shadow density, contrast curve, matte or clear look, haze, grain, and perceived dynamic range.
7. **Lens and perspective**: Infer likely focal length family, camera distance, compression, depth of field, viewpoint height, and distortion control.
8. **Editing direction**: Give plausible Lightroom/Camera Raw moves as ranges and relationships, not false exact values.
9. **Learning value**: End with 3 specific lessons the user can apply next time.

## Shoot-Like-This Plan

When the user asks how to shoot a similar sample, convert the analysis into an action plan:

1. **Scene recipe**: Suitable location type, background qualities, weather, time window, and environmental details to look for.
2. **Light setup**: Where the light should come from, how hard/soft it should be, how to use shade, windows, reflection, diffusion, or backlight.
3. **Camera position**: Where to stand, camera height, distance to subject, angle, and how much background to include.
4. **Focal length / phone lens**: Suggest camera focal length families and phone equivalents such as 1x, 2x, 3x, or portrait mode. Explain the visual tradeoff.
5. **Subject direction**: Pose, gesture, gaze, prop placement, clothing color, object arrangement, and what to simplify.
6. **Exposure priorities**: What to protect: highlights, skin, sky, shadow detail, or silhouette. Mention white balance intent.
7. **Shot list**: Provide 5-8 concrete frames to try, ordered from easiest to more refined.
8. **On-site checklist**: Give a short checklist the user can follow while shooting.
9. **Editing path**: Explain the post-processing route to reach the reference style.

## Lightroom and Camera Raw Guidance

Use parameter ranges only as practical guidance. Prefer relationships over exact imitation.

Cover these controls when relevant:

- **Basic**: Exposure, contrast, highlights, shadows, whites, blacks, texture, clarity, dehaze, vibrance, saturation.
- **Tone curve**: Whether to lift blacks, compress highlights, deepen midtones, add an S-curve, or soften contrast.
- **HSL / Color Mixer**: Hue shifts, saturation reductions, luminance separation, especially for sky, greens, skin, reds/oranges, and neutrals.
- **Color grading**: Shadow, midtone, and highlight tint; balance direction; warm/cool separation.
- **Calibration**: Use carefully for global color character, especially blue primary and red primary shifts.
- **Masking**: Local subject lift, face/skin refinement, background darkening, sky recovery, radial emphasis, and edge cleanup.
- **Effects**: Grain, vignette, bloom/softness, sharpening, and noise reduction when stylistically useful.

Always include the reason behind a recommendation. Example: "Lower green saturation and raise green luminance to make foliage quieter while keeping the scene fresh."

## Reference Match Workflow

When comparing a reference photo with the user's photo:

1. Start with a short verdict: what is already close and what most separates the two.
2. Rank differences by impact: light first, then composition, lens/perspective, color, tone, and local edits.
3. Separate **things to fix next time while shooting** from **things that can be improved in editing**.
4. Give a priority list with no more than 7 steps.
5. Be encouraging but specific. Avoid vague advice such as "make it more cinematic" unless followed by concrete changes.

## Output Formats

Use one of these structures depending on the request.

For reference analysis:

```markdown
**整体观感**
...

**构图**
...

**光线**
...

**色彩与影调**
...

**后期反推**
...

**你可以学的 3 点**
1. ...
2. ...
3. ...
```

For shoot-like-this planning:

```markdown
**样片拍法**
...

**现场条件**
...

**站位与构图**
...

**光线安排**
...

**拍摄参数思路**
...

**现场 shot list**
1. ...

**后期路径**
...
```

For reference match:

```markdown
**差距判断**
...

**优先调整**
1. ...

**下次拍摄这样做**
...

**这张图可以这样修**
...
```

## Quality Rules

- Be visually specific. Name what is visible: edge lines, color zones, light falloff, background separation, shadow density, highlight behavior.
- Distinguish observation from inference. Use phrases like "看起来像", "大概率", and "如果现场条件允许" when appropriate.
- Do not overfit to gear. Good advice should work for phone and camera users unless the user asks for a specific system.
- Prefer actionable advice over terminology. Explain technical terms briefly when they matter.
- Avoid fake precision. Do not invent exact EXIF, lens, preset, LUT, or original edit values.
- Keep the tone like a thoughtful photography mentor: appreciative, practical, and direct.
