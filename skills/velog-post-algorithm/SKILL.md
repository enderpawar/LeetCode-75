---
name: velog-post
description: Convert one or more algorithm problem solutions into a Korean Velog study post with a personal retrospective voice, verified solution logic, code, complexity analysis, stumbling points, and self-answered questions. Use when the user asks to write, revise, or format a coding-test, LeetCode, Baekjoon, or algorithm study note for Velog, especially from solution files, code snippets, debugging conversations, or weekly study notes.
---

# Velog Post

Write a publish-ready Korean Markdown post that sounds like the learner's own study record. Preserve the user's level, discoveries, and uncertainties instead of turning the post into a generic textbook explanation.

## Workflow

1. Gather the supplied problem statements, solution code, debugging history, and reflections. Inspect referenced local files when available.
2. Verify each algorithm before writing:
   - Trace representative and boundary cases.
   - Distinguish a correct core idea from implementation mistakes.
   - Correct Python terminology, return behavior, imports, and complexity claims.
   - Do not silently present broken code as correct. Use corrected final code and briefly explain meaningful corrections.
3. Choose one post-level theme connecting the problems, such as string basics, greedy thinking, or adapting to LeetCode.
4. For each problem, decide what is still improvable in the accepted solution and verify the improved version by tracing it, exactly as with the main solution.
5. Draft using the structure and voice rules in [references/post-pattern.md](references/post-pattern.md).
6. Perform a final editorial pass:
   - Keep terminology and variable names consistent.
   - Ensure every code block is fenced with its language.
   - Remove repetition between the explanation, key idea, and Q&A.
   - Preserve concrete personal observations supplied by the user.
   - Do not invent experiences, motivations, dates, study duration, or claims about external services.

## Input Handling

- If several solution files are available, group them into one weekly post when the user asks for a study recap.
- If only code is supplied, infer the algorithmic explanation but not personal feelings. Phrase inferred difficulties neutrally or omit them.
- If the user's original approach was partially correct, say precisely which idea was right and which implementation details failed.
- If essential context is missing, produce the strongest useful draft with placeholders only for indispensable facts.

## Output Requirements

- Return only the polished post unless the user asks for review notes or alternatives.
- Format the title as `[Series Day N] Algorithm1, Algorithm2`, using the English names of the algorithms or data structures most directly related to that day's solved problems. Do not use a descriptive Korean theme in the title. For example, use `[LeetCode 75 Day 7] LinkedList, Queue` for a day covering linked-list and queue problems.
- Use natural Korean prose and Markdown suitable for direct pasting into Velog.
- Prefer paragraphs over excessive bullets. Use numbered steps only when they clarify an algorithm.
- Keep beginner-oriented explanations concrete: explain what syntax does in the code at hand.
- Include time and space complexity for each problem when they can be determined.
- End every problem section with a `### 더 개선한다면` reflection plus an improved code block, as specified in the reference. The reflection may not be replaced by a generic "이 정도면 충분하다" remark.
- Do not add a table of contents, tags, emoji, promotional closing, or references unless requested.
- Keep the main code block faithful to the verified solution and avoid unrelated optimization. Optimizations and rewrites belong in the improvement reflection, never folded silently into the main block.

## Quality Bar

Before returning the post, confirm:

- The title lists the day's relevant algorithms or data structures in English.
- The introduction explains the study context without exaggeration.
- Each problem section contains the task, code, core idea, actual stumbling points, and a closing improvement reflection.
- Every improved code block was traced, differs meaningfully from the solution above it, and names its trade-off or new complexity.
- The Q&A resolves genuine confusions rather than padding the post.
- The conclusion summarizes what changed in the learner's understanding and points naturally to the next step.
