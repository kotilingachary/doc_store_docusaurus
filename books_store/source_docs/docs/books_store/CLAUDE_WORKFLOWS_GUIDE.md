# Claude Workflows Usage Guide

**Quick Start Guide for Team Members**

## What Are Claude Workflows?

Claude workflows are AI-powered GitHub Actions that go beyond basic automation to provide intelligent code improvements using Anthropic's Claude AI.

**Prefix:** All Claude workflows use the `claude-` prefix (vs `std-` for standard actions)

---

## Available Workflows

### 🤖 claude-code-quality.yml

**Purpose:** AI-powered comprehensive code quality enhancement

**What it does:**
- ✅ Everything `std-format.yml` does (Google Java Format)
- ✅ Adds comprehensive JavaDoc documentation
- ✅ Improves variable and method naming
- ✅ Adds validation annotations
- ✅ Fixes null safety issues
- ✅ Corrects HTTP status codes
- ✅ Enforces Spring Boot best practices
- ✅ Posts educational PR comments

**When to use:**
- Before submitting code for review
- On new features
- When adding public APIs
- To improve code quality

**Cost:** ~$0.10-0.30 per run (covered by team budget)
**Time:** 1-2 minutes

---

## How to Use

### Method 1: Manual Trigger (Easiest)

1. Go to: [Actions Tab](../../actions)
2. Select: **"Claude Code Quality Enhancement"**
3. Click: **"Run workflow"**
4. Select:
   - **Branch:** Your feature branch
   - **Scope:**
     - `changed-files` (default - only recent changes)
     - `all-files` (entire codebase)
     - `specific-package` (target a package)
5. Click: **"Run workflow"**

**Wait 1-2 minutes** → Claude will analyze and improve your code

---

### Method 2: Comment Trigger (In PRs)

In any Pull Request, add a comment:

```
@claude improve code quality
```

Claude will automatically:
1. Analyze your PR code
2. Make quality improvements
3. Commit changes
4. Post detailed explanation

**Example:**
```markdown
PR #123: Add book search feature

Comments:
- @jane: LGTM, just minor formatting issues
- @you: @claude improve code quality
- [Claude runs and improves code]
- @claude: [Posts detailed improvements]
```

---

### Method 3: Scheduled (Coming Soon)

**Currently disabled** - Will be enabled after testing phase

Planned: Weekly quality review every Friday before sprint review

---

## What to Expect

### Typical Improvements

**Before Claude:**
```java
public ResponseEntity createBook(@RequestBody Book book){
if(book.getName()==null)throw new Exception("error");
Book b=bookService.save(book);
return ResponseEntity.ok(b);}
```

**After Claude:**
```java
/**
 * Creates a new book in the system.
 *
 * <p>Validates the book data and persists it to the database.
 *
 * @param book the book to create (must not be null and pass validation)
 * @return ResponseEntity containing the created book with 201 status
 * @throws IllegalArgumentException if book validation fails
 */
@PostMapping
public ResponseEntity<Book> createBook(@Valid @RequestBody Book book) {
    if (book.getName() == null || book.getName().isEmpty()) {
        throw new IllegalArgumentException("Book name is required and cannot be empty");
    }

    Book createdBook = bookService.save(book);
    return ResponseEntity.status(HttpStatus.CREATED).body(createdBook);
}
```

---

### Claude's PR Comment

When Claude finishes, it posts a detailed comment like:

```markdown
## 🎨 Code Quality Improvements

I've enhanced your code with the following improvements:

### ✅ Documentation
- Added JavaDoc to BookController class
- Documented createBook() method with examples

### ✨ Naming
- Improved: `Book b` → `Book createdBook`

### 🔒 Validation
- Added @Valid annotation for automatic validation
- Enhanced error message clarity

### 🌐 HTTP Semantics
- Fixed: 200 OK → 201 CREATED (correct for resource creation)

### 📊 Quality Score
- Before: 62/100
- After: 88/100 (+26 points)

All changes preserve functionality while improving maintainability.
```

---

## Comparison with Standard Format

| Feature | std-format.yml | claude-code-quality.yml |
|---------|----------------|------------------------|
| Speed | ⚡ 30 seconds | 🐌 1-2 minutes |
| Cost | 💰 Free | 💰 ~$0.25 |
| Formatting | ✅ Yes | ✅ Yes |
| Documentation | ❌ No | ✅ Yes |
| Naming | ❌ No | ✅ Yes |
| Validation | ❌ No | ✅ Yes |
| Best Practices | ❌ No | ✅ Yes |
| Explanations | ❌ No | ✅ Yes |

**Recommendation:** Use both!
- `std-format` runs automatically on every commit (fast, free)
- `claude-code-quality` runs when you need deep improvements (smart, valuable)

---

## Best Practices

### ✅ DO Use Claude When:
- Finishing a new feature
- Before submitting for review
- Adding public APIs
- Code needs documentation
- Quality improvements needed
- Learning best practices

### ⚠️ DON'T Use Claude When:
- Quick formatting fixes (use `std-format` instead)
- Every single commit (too expensive)
- Code is already high quality
- Just fixing typos

---

## FAQ

### Q: Will Claude change my business logic?
**A:** No. Claude is instructed to ONLY improve code quality without changing functionality. If it detects logic issues, it will comment but not change.

### Q: What if I don't like Claude's changes?
**A:** Simply revert the commit:
```bash
git revert HEAD
git push
```
You can also modify the prompt in the workflow file to adjust Claude's behavior.

### Q: How much does this cost?
**A:** ~$0.10-0.30 per run. Team budget covers this. For perspective, one run costs less than 5 minutes of developer time but saves 20-30 minutes.

### Q: Can I customize what Claude checks?
**A:** Yes! Edit `.github/workflows/claude-code-quality.yml` and modify the prompt to add/remove focus areas.

### Q: Will this slow down my workflow?
**A:** No. `std-format` still runs fast on every commit. Claude only runs when you explicitly trigger it.

### Q: What if Claude makes a mistake?
**A:** Review all changes before merging (as you would any code review). Claude is very accurate but not perfect.

---

## Troubleshooting

### Error: "ANTHROPIC_API_KEY not found"
**Solution:** Contact DevOps team to add the API key to GitHub secrets.

### Error: "Workflow run failed"
**Solutions:**
1. Check the logs in the Actions tab
2. Verify branch permissions
3. Contact team lead

### Claude didn't post a comment
**Possible reasons:**
1. Comment trigger requires exact text: `@claude improve code quality`
2. Must be in a PR (not an issue)
3. Check Actions tab for workflow status

### Changes look wrong
**Action:**
1. Review the changes carefully
2. If incorrect, revert: `git revert HEAD`
3. Report issue to team lead with example
4. We'll refine the prompts

---

## Getting Help

- **Documentation:** `docs/Analysis/Claude-vs-Standard-Actions-Comparison.md`
- **Team Lead:** [Your Name]
- **Slack Channel:** #dev-tools
- **GitHub Issues:** Tag with `claude-workflow`

---

## Roadmap

### ✅ Current (Phase 1)
- Manual trigger
- Comment trigger (`@claude improve`)
- Code quality enhancement

### 🚧 Coming Soon (Phase 2)
- Scheduled weekly quality reviews
- Label-based auto-triggers
- Security audit workflow
- Auto-test fixer

### 🔮 Future (Phase 3)
- Custom code review rules
- Team coding standards enforcement
- Automated refactoring suggestions
- Integration with sprint metrics

---

## Quick Reference Card

**Print this or save to desktop:**

```
┌─────────────────────────────────────────────────┐
│   Claude Workflows - Quick Reference           │
├─────────────────────────────────────────────────┤
│                                                 │
│  🎯 Improve Code Quality:                      │
│     Comment in PR: @claude improve code quality │
│                                                 │
│  🚀 Manual Trigger:                            │
│     Actions → Claude Code Quality → Run        │
│                                                 │
│  ⏱️  Time: 1-2 minutes                         │
│  💰 Cost: ~$0.25                               │
│  📈 Value: 20-30 min saved                     │
│                                                 │
│  📚 Full Docs:                                 │
│     docs/CLAUDE_WORKFLOWS_GUIDE.md             │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

**Last Updated:** September 30, 2025
**Version:** 1.0
**Status:** Active - Testing Phase
