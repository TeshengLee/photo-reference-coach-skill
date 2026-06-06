# Photography Coach

`photography-coach` is a multilingual Codex skill for practical photography coaching.

It analyzes composition, light, color, tone, EXIF/GPS, shooting technique, style references, and editing workflows. It can explain a sample, diagnose a user's photo, plan a similar shoot, or teach adjustments inside the user's actual editing app.

## Supported Languages

The skill is designed to respond in the user's language by default and explicitly supports:

- English
- Chinese
- Japanese
- Korean
- French
- German
- Spanish
- Portuguese

## Skill

The skill lives in:

```text
photography-coach/
```

## Install

### Option 1: Ask Codex to install it

In Codex, ask:

```text
Use $skill-installer to install https://github.com/TeshengLee/photography-coach-skill/tree/main/photography-coach
```

Restart Codex after installation so the new skill is picked up.

### Option 2: Install with the skill installer script

If you have the OpenAI skill installer available locally, run:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo TeshengLee/photography-coach-skill \
  --path photography-coach
```

Restart Codex after installation.

### Option 3: Manual install

Clone or download this repository, then copy the `photography-coach/` folder into your Codex skills directory:

```text
~/.codex/skills/photography-coach/
```

If your Codex setup uses a different skills directory, copy it there instead. Restart Codex after copying.

## Usage

Invoke the skill explicitly with:

```text
$photography-coach
```

For example:

```text
$photography-coach Analyze this photo: composition, light, color, editing, and how to shoot a similar image.
```

## Language and Token Use

This is one multilingual skill, not eight separate installed skills. The skill responds in the language used by the user prompt; it does not auto-select based on the computer's system language.

The core `SKILL.md` is intentionally compact. The style reference material lives in `photography-coach/references/style-library.md` and is only meant to be loaded when style diagnosis or no-sample improvement needs it.

## Typical Prompts

English:

```text
$photography-coach Analyze this photo: composition, light, color, editing, and how to shoot a similar image.
```

Chinese:

```text
$photography-coach 分析这张照片，从构图到调色讲清楚。
```

Japanese:

```text
$photography-coach この写真の構図、光、色、レタッチ、似た雰囲気で撮る方法を分析してください。
```

Korean:

```text
$photography-coach 이 사진의 구도, 빛, 색감, 보정 방향과 비슷하게 촬영하는 방법을 분석해 주세요.
```

French:

```text
$photography-coach Analyse cette photo : composition, lumière, couleurs, retouche, et comment réaliser une image similaire.
```

German:

```text
$photography-coach Analysiere dieses Foto: Komposition, Licht, Farben, Bearbeitung und wie ich ein ähnliches Bild aufnehmen kann.
```

Spanish:

```text
$photography-coach Analiza esta foto: composición, luz, color, edición y cómo tomar una imagen similar.
```

Portuguese:

```text
$photography-coach Analise esta foto: composição, luz, cor, edição e como fotografar uma imagem parecida.
```

Shoot planning:

```text
$photography-coach 我想拍出类似样片，给我一个现场拍摄方案。
```

Reference matching:

```text
$photography-coach 参考图是第一张，我拍的是第二张，告诉我下次怎么拍、这张怎么修。
```

## Capabilities

- Reference photo aesthetic analysis
- Composition and subject-placement breakdown
- Light direction and light-quality inference
- Color and tone analysis
- Lightroom / Camera Raw editing direction
- Practical shoot-like-this plans for similar scenes
- Reference matching against the user's own image
- Concrete shooting starting values for camera and phone users
- Tool-specific parameter ranges and adjustment logic
- Automatic, non-blocking EXIF/GPS preflight for accessible attachments
- Separate phone and interchangeable-lens camera workflows
- App-matched instructions, including Apple Photos and Instagram paths

## License

MIT
