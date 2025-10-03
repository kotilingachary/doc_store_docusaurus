# Claude Code Setup Training Plan

**Project**: Spring Boot Book Management System
**Purpose**: Comprehensive guide to understand the current Claude Code configuration
**Audience**: Developers, team members, and stakeholders exploring the project setup

---

## 🎯 **Starting Point: Where to Begin**

**First File to Read:** `CLAUDE.md`
- Location: `/Basics_Lab_1/CLAUDE.md`
- Purpose: Primary Claude Code configuration file
- Contains: Development commands, architecture overview, agent summary
- Time needed: 5 minutes

**Why start here?** This file is what Claude Code reads first when working with your project.

---

## 📋 **Complete Exploration Sequence**

### **Phase 1: Project Overview (5 minutes)**
```bash
# Read the main configuration
cat CLAUDE.md

# Check overall project structure
ls -la

# See what documentation folders exist
ls */README.md

# Quick architecture check
grep -A 5 "Architecture" CLAUDE.md
```

**What you'll learn:** Project scope, main commands, basic architecture

### **Phase 2: Active Claude Configuration (10 minutes)**
```bash
# Explore currently active agents (16 total)
find .claude/agents -name "*.md" | wc -l
find .claude/agents -name "*.md" | head -5

# Look at a sample agent
cat docs/claude-config/agents/development-review/code-reviewer.md

# Explore active commands (9 total)
find .claude/commands -name "*.md" | wc -l
find .claude/commands -name "*.md" | head -3

# Read command overview
cat docs/claude-config/commands/README.md

# Understand active vs dormant setup
cat .claude/README.md
```

**What you'll learn:** Current Claude capabilities, available commands, active vs dormant architecture

### **Phase 3: Business Understanding (10 minutes)**
```bash
# Read business requirements
cat docs/requirements/REQUIREMENTS.md | head -30

# Check user stories
grep -E "US-[0-9]+" docs/requirements/REQUIREMENTS.md

# Understand architecture
cat docs/architecture/ARCHITECTURE.md | head -30

# See project analysis
cat docs/analysis/README.md

# Check what the API does
grep -A 10 "API Endpoints" CLAUDE.md
```

**What you'll learn:** What the system does, user requirements, technical architecture

### **Phase 4: Enterprise Capabilities (Optional - 5 minutes)**
```bash
# See future scaling options
cat docs/claude-config/agents-enterprise/README.md

# Understand activation process
cat docs/claude-config/ACTIVATION_GUIDE.md | head -50

# Check dormant agent count
find .claude/agents-enterprise -name "*.md" | wc -l

# See dormant command count
find .claude/commands-enterprise -name "*.md" | wc -l
```

**What you'll learn:** Future capabilities, scaling strategy, enterprise readiness

---

## 🗺️ **Essential Files Reference**

### **Must Read Files (Core Understanding)**
1. **`CLAUDE.md`** - Main Claude Code configuration and commands
2. **`.claude/README.md`** - Active vs dormant architecture explanation
3. **`docs/requirements/REQUIREMENTS.md`** - Business requirements and user stories
4. **`docs/architecture/ARCHITECTURE.md`** - Technical architecture and design

### **Important Files (Development Ready)**
5. **`docs/claude-config/commands/README.md`** - Available development commands
6. **`docs/analysis/README.md`** - Project analysis and insights
7. **`docs/claude-config/agents/development-review/code-reviewer.md`** - Example agent configuration

### **Advanced Files (Full Mastery)**
8. **`docs/claude-config/agents-enterprise/README.md`** - Enterprise capabilities overview
9. **`docs/claude-config/ACTIVATION_GUIDE.md`** - How to scale up capabilities
10. **`docs/analysis/business-logic-compliance-analysis.md`** - Implementation compliance

---

## 🎓 **Learning Levels & Time Investment**

### **Level 1: Basic Understanding (10 minutes)**
**Goal:** Know what the project does and how to start it

**Read:**
- `CLAUDE.md` (main config)
- `docs/requirements/REQUIREMENTS.md` (first 20 lines)
- `.claude/README.md` (architecture overview)

**Commands:**
```bash
head -30 CLAUDE.md
grep "mvn spring-boot:run" CLAUDE.md
grep -E "US-[0-9]+" docs/requirements/REQUIREMENTS.md | head -5
```

**You'll Know:** Project purpose, how to start it, basic agent setup

### **Level 2: Development Ready (20 minutes)**
**Goal:** Ready to work with Claude Code on this project

**Additional Reading:**
- Active agents overview
- Available commands
- Project architecture

**Commands:**
```bash
find .claude/agents -name "*.md" | sed 's/.*\///' | sed 's/\.md//'
cat docs/claude-config/commands/README.md
grep -A 15 "API Endpoints" CLAUDE.md
```

**You'll Know:** All active capabilities, development commands, system architecture

### **Level 3: Full Mastery (30 minutes)**
**Goal:** Complete understanding including future scaling

**Additional Reading:**
- Enterprise capabilities
- Activation strategies
- Analysis documents

**Commands:**
```bash
cat docs/claude-config/ACTIVATION_GUIDE.md
find .claude/agents-enterprise -name "*.md" | wc -l
cat docs/analysis/business-logic-compliance-analysis.md | head -20
```

**You'll Know:** Complete setup, scaling strategy, enterprise readiness

---

## 🔍 **Quick Understanding Commands**

### **Project Scope**
```bash
# What does the system do?
grep -A 5 "Book Management" docs/requirements/REQUIREMENTS.md

# How many user stories?
grep -c "US-" docs/requirements/REQUIREMENTS.md

# What's the main API?
grep -A 8 "API Endpoints" CLAUDE.md
```

### **Claude Setup**
```bash
# How many active agents?
find .claude/agents -name "*.md" | wc -l

# What agents are active?
find .claude/agents -name "*.md" | sed 's/.*\///' | sed 's/\.md//' | sort

# How many dormant capabilities?
find .claude/agents-enterprise -name "*.md" | wc -l
```

### **Development Info**
```bash
# How to start the app?
grep "mvn spring-boot:run" CLAUDE.md

# How to test?
grep "mvn test" CLAUDE.md

# What's the API URL?
grep "localhost:8080" CLAUDE.md
```

---

## 🧪 **Test Your Understanding**

### **Basic Level Test**
1. **Q:** How do you start the application?
   **A:** `mvn spring-boot:run`

2. **Q:** What port does it run on?
   **A:** `8080` (check with `grep "8080" CLAUDE.md`)

3. **Q:** How many active agents are configured?
   **A:** Run `find .claude/agents -name "*.md" | wc -l`

### **Intermediate Level Test**
1. **Q:** What are the main API endpoints?
   **A:** Check `grep -A 8 "API Endpoints" CLAUDE.md`

2. **Q:** How many user stories are implemented?
   **A:** Run `grep -c "US-" docs/requirements/REQUIREMENTS.md`

3. **Q:** What's the difference between active and dormant agents?
   **A:** Read `.claude/README.md` active vs dormant section

### **Advanced Level Test**
1. **Q:** How do you activate a dormant agent?
   **A:** Use `mv` commands from `docs/claude-config/ACTIVATION_GUIDE.md`

2. **Q:** When would you activate enterprise agents?
   **A:** Production launch, enterprise customers, microservices (see activation guide)

3. **Q:** What's the current implementation compliance score?
   **A:** Check `docs/analysis/business-logic-compliance-analysis.md`

---

## 🚀 **Ready-to-Use Commands After Training**

### **Development Commands**
```bash
# Start the application
mvn spring-boot:run

# Run all tests
mvn test

# Build the project
mvn clean package

# Test coverage
mvn test jacoco:report
```

### **API Testing Commands**
```bash
# Test the API
curl localhost:8080/books

# Health check
curl localhost:8080/actuator/health

# Create a book (example)
curl -X POST -H "Content-Type: application/json" \
  -d '{"title":"Test Book","author":"Test Author","isbn":"123"}' \
  localhost:8080/books
```

### **Claude Code Integration**
```bash
# If Claude Code is available, list agents
claude-code --list-agents

# List available commands
claude-code --list-commands

# Run specific agent (example)
claude-code run-agent code-reviewer
```

---

## 📚 **Additional Learning Resources**

### **Explore Further**
- **Demo Data**: Check `docs/demo/` folder for sample CSV files and API specs
- **Product Requirements**: Read `docs/product/PRD.md` for business context
- **Analysis Reports**: Explore `docs/analysis/` folder for detailed project insights

### **When You're Ready to Scale**
- **Enterprise Agents**: Browse `.claude/agents-enterprise/` folders
- **Advanced Commands**: Check `.claude/commands-enterprise/` capabilities
- **Activation Examples**: Follow `docs/claude-config/ACTIVATION_GUIDE.md` scenarios

### **Troubleshooting**
- **Build Issues**: Check `CLAUDE.md` build troubleshooting section
- **Java Setup**: Look for JAVA_HOME configuration in `CLAUDE.md`
- **API Issues**: Verify application is running on port 8080

---

## ⏱️ **Training Completion Checklist**

### **✅ Basic Level (10 minutes)**
- [ ] Read `CLAUDE.md` main configuration
- [ ] Understand project purpose from `docs/requirements/REQUIREMENTS.md`
- [ ] Know how to start the application
- [ ] Understand active vs dormant agent architecture

### **✅ Development Level (20 minutes)**
- [ ] Explored active agents and commands
- [ ] Understand API endpoints and functionality
- [ ] Know development workflow commands
- [ ] Can test the running application

### **✅ Advanced Level (30 minutes)**
- [ ] Understand enterprise scaling capabilities
- [ ] Know when and how to activate dormant agents
- [ ] Familiar with analysis and compliance reports
- [ ] Ready to guide others through the setup

**Congratulations! You now understand the complete Claude Code setup for this Spring Boot Book Management project.**
