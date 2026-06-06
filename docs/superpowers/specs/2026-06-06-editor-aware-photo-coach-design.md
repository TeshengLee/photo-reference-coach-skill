# Editor-Aware Photo Coach Design

The skill must automatically attempt metadata extraction whenever an accessible local image file exists. Missing metadata never blocks analysis and never requires another upload.

Editing guidance is gated by the user's editor. If no editor is known, ask one short question before giving detailed adjustment steps. Then use only controls available in that editor and include the navigation path, control name, starting value, and visual checkpoint.

Keep core rules in `SKILL.md`; place app-specific mappings in one concise on-demand reference.
