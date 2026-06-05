# Photo Reference Coach

`photo-reference-coach` is a Codex skill for learning from strong photography references.

It helps an agent analyze a photo from composition, light, color, tone, editing style, and practical reproduction strategy. It is designed for photographers who see a reference image and want to understand both why it works and how to shoot or edit toward a similar result.

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
photo-reference-coach/
```

## Install

### Option 1: Ask Codex to install it

In Codex, ask:

```text
Use $skill-installer to install https://github.com/TeshengLee/photo-reference-coach-skill/tree/main/photo-reference-coach
```

Restart Codex after installation so the new skill is picked up.

### Option 2: Install with the skill installer script

If you have the OpenAI skill installer available locally, run:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo TeshengLee/photo-reference-coach-skill \
  --path photo-reference-coach
```

Restart Codex after installation.

### Option 3: Manual install

Clone or download this repository, then copy the `photo-reference-coach/` folder into your Codex skills directory:

```text
~/.codex/skills/photo-reference-coach/
```

If your Codex setup uses a different skills directory, copy it there instead. Restart Codex after copying.

## Usage

Invoke the skill explicitly with:

```text
$photo-reference-coach
```

For example:

```text
$photo-reference-coach Analyze this photo: composition, light, color, editing, and how to shoot a similar image.
```

## Typical Prompts

English:

```text
$photo-reference-coach Analyze this photo: composition, light, color, editing, and how to shoot a similar image.
```

Chinese:

```text
$photo-reference-coach 分析这张照片，从构图到调色讲清楚。
```

Japanese:

```text
$photo-reference-coach この写真の構図、光、色、レタッチ、似た雰囲気で撮る方法を分析してください。
```

Korean:

```text
$photo-reference-coach 이 사진의 구도, 빛, 색감, 보정 방향과 비슷하게 촬영하는 방법을 분석해 주세요.
```

French:

```text
$photo-reference-coach Analyse cette photo : composition, lumière, couleurs, retouche, et comment réaliser une image similaire.
```

German:

```text
$photo-reference-coach Analysiere dieses Foto: Komposition, Licht, Farben, Bearbeitung und wie ich ein ähnliches Bild aufnehmen kann.
```

Spanish:

```text
$photo-reference-coach Analiza esta foto: composición, luz, color, edición y cómo tomar una imagen similar.
```

Portuguese:

```text
$photo-reference-coach Analise esta foto: composição, luz, cor, edição e como fotografar uma imagem parecida.
```

Shoot planning:

```text
$photo-reference-coach 我想拍出类似样片，给我一个现场拍摄方案。
```

Reference matching:

```text
$photo-reference-coach 参考图是第一张，我拍的是第二张，告诉我下次怎么拍、这张怎么修。
```

## Capabilities

- Reference photo aesthetic analysis
- Composition and subject-placement breakdown
- Light direction and light-quality inference
- Color and tone analysis
- Lightroom / Camera Raw editing direction
- Practical shoot-like-this plans for similar scenes
- Reference matching against the user's own image

## License

MIT
