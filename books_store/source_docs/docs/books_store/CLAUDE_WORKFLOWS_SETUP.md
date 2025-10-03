# Claude Workflows - Setup Checklist

**One-time setup required before using Claude workflows**

## Prerequisites

### 1. Anthropic API Key ✅

#### Step 1: Create Anthropic Account
1. Go to: https://console.anthropic.com
2. Sign up with email or Google/GitHub account
3. Verify email if required

#### Step 2: Generate API Key
1. Navigate to: **API Keys** section
2. Click: **"Create Key"**
3. Name: `GitHub-Actions-CodeAI`
4. Copy the key (starts with `sk-ant-api...`)
5. **⚠️ Save it securely** - you won't see it again

#### Step 3: Add to GitHub Secrets
1. Go to: https://github.com/kotilingachary/CodeAI/settings/secrets/actions
2. Click: **"New repository secret"**
3. Enter:
   - **Name:** `ANTHROPIC_API_KEY`
   - **Value:** `sk-ant-api...` (your key from Step 2)
4. Click: **"Add secret"**

#### Step 4: Verify Setup
1. Go to: https://github.com/kotilingachary/CodeAI/actions
2. Select: **"Claude Code Quality Enhancement"**
3. Click: **"Run workflow"**
4. Select branch: `ClaudeCode`
5. Click: **"Run workflow"**
6. Wait ~1-2 minutes
7. Check if workflow succeeds ✅

If you see error: "ANTHROPIC_API_KEY not found" → Go back to Step 3

---

### 2. GitHub Permissions ✅

Already configured! ✅ (Done earlier in the session)

Repository permissions allow:
- ✅ Creating branches
- ✅ Creating PRs
- ✅ Posting comments
- ✅ Committing code

---

### 3. Budget Allocation

#### Cost Estimate
- **Per Run:** $0.10 - $0.30
- **Estimated Usage:** 10-20 runs/month (testing phase)
- **Monthly Cost:** $2 - $6
- **Annual Cost:** $24 - $72

#### Budget Approval
- [ ] Budget allocated: $10/month (buffer included)
- [ ] Approved by: _________________
- [ ] Date: _________________

---

### 4. Team Notification

- [ ] Team notified about new Claude workflows
- [ ] Usage guide shared: `docs/CLAUDE_WORKFLOWS_GUIDE.md`
- [ ] Q&A session scheduled (optional)
- [ ] Feedback channel created (e.g., #claude-workflows)

---

## Testing Checklist

### Test 1: Manual Trigger
- [ ] Navigate to Actions tab
- [ ] Select "Claude Code Quality Enhancement"
- [ ] Run on `ClaudeCode` branch
- [ ] Verify workflow completes successfully
- [ ] Review changes committed
- [ ] Check quality of improvements

### Test 2: Comment Trigger
- [ ] Create a test PR
- [ ] Add comment: `@claude improve code quality`
- [ ] Verify workflow triggers automatically
- [ ] Check PR comment posted by Claude
- [ ] Review code changes
- [ ] Verify educational value of explanations

### Test 3: Different Scopes
- [ ] Test with `changed-files` scope
- [ ] Test with `all-files` scope
- [ ] Test with `specific-package` scope
- [ ] Verify each scope works correctly

---

## Rollout Plan

### Phase 1: Limited Testing (Week 1-2) ✅ ← YOU ARE HERE
- [x] Setup workflow file
- [x] Add API key to secrets
- [ ] Test manually 3-5 times
- [ ] Collect initial feedback
- [ ] Adjust prompts if needed
- **Goal:** Verify workflow works correctly

### Phase 2: Team Testing (Week 3-4)
- [ ] Share usage guide with team
- [ ] Enable comment trigger for all team members
- [ ] Each team member tests on 1-2 PRs
- [ ] Collect feedback via survey
- [ ] Calculate actual costs
- [ ] Measure time saved
- **Goal:** Team comfortable using it

### Phase 3: Regular Use (Month 2+)
- [ ] Enable scheduled weekly runs
- [ ] Enable label-based triggers
- [ ] Make it part of PR checklist (optional)
- [ ] Track ROI metrics
- [ ] Optimize based on usage patterns
- **Goal:** Full integration into workflow

---

## Monitoring Setup

### Cost Tracking
1. **Anthropic Console**
   - Check usage: https://console.anthropic.com/settings/usage
   - Set budget alert: $10/month threshold
   - Review weekly

2. **Spreadsheet Tracking**
   - Date | Workflow | Cost | Time Saved | Notes
   - Track for first month
   - Calculate ROI

### Usage Metrics
Track in first month:
- [ ] Number of runs
- [ ] Average cost per run
- [ ] Average time taken
- [ ] Success rate
- [ ] Team satisfaction (1-5 survey)

---

## Configuration Options

### Customizing the Workflow

**File:** `.github/workflows/claude-code-quality.yml`

#### Enable Scheduled Runs
Uncomment lines 50-52:
```yaml
schedule:
  # Every Friday at 10 AM UTC (before sprint review)
  - cron: "0 10 * * 5"
```

#### Enable Label Triggers
Uncomment lines 55-57:
```yaml
pull_request:
  types: [labeled, opened]
```

Then update line 75 to include:
```yaml
if: |
  github.event_name == 'workflow_dispatch' ||
  (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@claude improve')) ||
  github.event_name == 'schedule' ||
  (github.event_name == 'pull_request' &&
   (contains(github.event.pull_request.labels.*.name, 'enhancement') ||
    contains(github.event.pull_request.labels.*.name, 'feature')))
```

#### Adjust Scope
Change default scope in line 36:
```yaml
default: 'changed-files'  # or 'all-files' or 'specific-package'
```

#### Customize Prompts
Edit lines 115-350 to add/remove focus areas or examples

---

## Troubleshooting

### Issue: API Key Error
```
Error: ANTHROPIC_API_KEY not found
```
**Solution:**
1. Verify secret exists: Settings → Secrets → Actions
2. Check exact name: `ANTHROPIC_API_KEY` (case-sensitive)
3. Re-create secret if needed
4. Test again

---

### Issue: Workflow Not Triggering
**Comment Trigger:**
- Exact text required: `@claude improve code quality`
- Must be in PR (not issue)
- Check Actions tab for errors

**Manual Trigger:**
- Verify you have write permissions
- Check branch exists
- Try different branch

---

### Issue: High Costs
If costs exceed budget:
1. **Reduce Frequency**
   - Use manual trigger only
   - Disable scheduled runs
   - Be selective about when to use

2. **Limit Scope**
   - Use `changed-files` instead of `all-files`
   - Target specific packages only

3. **Adjust Prompts**
   - Reduce max-turns (line 356): `--max-turns 15` → `--max-turns 10`
   - Simplify instructions

---

### Issue: Poor Quality Improvements
If Claude's changes aren't helpful:
1. **Provide Examples**
   - Add more examples to prompt (lines 280-340)
   - Show your preferred style

2. **Add Constraints**
   - Add "DO NOT" rules to prompt
   - Specify what NOT to change

3. **Adjust Focus Areas**
   - Remove areas that aren't valuable
   - Add areas that are missing

---

## Security Considerations

### API Key Security
- ✅ API key stored in GitHub Secrets (encrypted)
- ✅ Never logged or exposed in workflow
- ✅ Limited to this repository only
- ⚠️ Rotate key every 6 months

### Code Security
- ✅ Claude only analyzes code in your repo
- ✅ No code sent to third parties except Anthropic
- ✅ Anthropic's data policy: https://www.anthropic.com/privacy
- ⚠️ Review Anthropic's privacy policy annually

### Workflow Security
- ✅ Requires write permissions (necessary for commits)
- ✅ Only runs on approved triggers
- ✅ All changes visible in commits
- ⚠️ Review all Claude commits before merging

---

## Success Criteria

After Phase 1 (Testing):
- [ ] Workflow runs successfully 5 times
- [ ] No errors or failures
- [ ] Code improvements are high quality
- [ ] Costs within budget
- [ ] Team finds it valuable

After Phase 2 (Team Testing):
- [ ] 3+ team members tested successfully
- [ ] Average satisfaction score >4/5
- [ ] Time saved >30 min per use
- [ ] No major issues reported
- [ ] Ready for regular use

After Phase 3 (Regular Use):
- [ ] Integrated into workflow
- [ ] ROI >500%
- [ ] Team satisfaction maintained
- [ ] Costs predictable
- [ ] Continuous value delivered

---

## Next Steps

### Immediate (Today)
1. [ ] Create Anthropic account
2. [ ] Generate API key
3. [ ] Add to GitHub secrets
4. [ ] Test manual trigger once
5. [ ] Verify workflow succeeds

### This Week
6. [ ] Test manual trigger 2-3 more times
7. [ ] Test comment trigger in a PR
8. [ ] Review code quality improvements
9. [ ] Collect initial feedback
10. [ ] Adjust prompts if needed

### Next Week
11. [ ] Share guide with 1-2 team members
12. [ ] Have them test on their PRs
13. [ ] Collect feedback
14. [ ] Calculate costs
15. [ ] Decide on Phase 3 rollout

---

## Support

### Getting Help
- **Documentation:** `docs/CLAUDE_WORKFLOWS_GUIDE.md`
- **Comparison:** `docs/Analysis/Claude-vs-Standard-Actions-Comparison.md`
- **Use Cases:** `docs/Analysis/Claude-GitHub-Integration-Use-Cases.md`

### Contacts
- **Technical Issues:** DevOps team
- **Usage Questions:** Team Lead
- **Cost/Budget:** Finance team
- **Anthropic Support:** https://support.anthropic.com

---

## Checklist Summary

**Setup Complete When:**
- [x] Workflow file created (`.github/workflows/claude-code-quality.yml`)
- [x] Documentation created (`CLAUDE_WORKFLOWS_GUIDE.md`, `CLAUDE_WORKFLOWS_SETUP.md`)
- [ ] Anthropic API key generated
- [ ] API key added to GitHub secrets
- [ ] Manual test run successful
- [ ] Team notified
- [ ] Budget allocated

**Current Status:** Setup 60% complete ⚠️

**Next Action:** Generate API key and add to GitHub secrets

---

**Last Updated:** September 30, 2025
**Version:** 1.0
**Status:** Setup in Progress
