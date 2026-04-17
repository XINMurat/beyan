# Module: Collaboration & Real-Time Testing

**Priority**: P1 (High - Critical for Collaborative Features)  
**Module Code**: **COLLAB-TEST**  
**Tokens**: ~3500  
**Analysis Time**: 25-35 minutes (Phase 1), 20-30 minutes (Phase 2), 15-20 minutes (Phase 3)  

---

## Purpose

Real-time collaboration özellikleri için test senaryoları ve executable tests oluşturur. WebSocket/SignalR, multi-user editing, concurrent changes, conflict resolution, presence indicators, live cursors ve operational transform (OT/CRDT) gibi collaboration patterns'ı test eder.

---

## 🎯 Collaboration Testing Challenges

```yaml
unique_challenges:
  real_time_sync:
    problem: "Değişiklikler diğer kullanıcılara anında yansımalı"
    test: "User A edits → User B sees change < 200ms"
  
  concurrent_editing:
    problem: "İki kullanıcı aynı anda aynı yeri editliyor"
    test: "User A & B edit same component → No data loss"
  
  conflict_resolution:
    problem: "Çakışan değişiklikler nasıl handle ediliyor?"
    test: "Conflicting changes merge correctly (OT/CRDT)"
  
  connection_resilience:
    problem: "Bağlantı koptuğunda ne oluyor?"
    test: "Disconnect → Reconnect → State recovered"
  
  presence_awareness:
    problem: "Diğer kullanıcılar görünüyor mu?"
    test: "User joins → Avatar appears, User leaves → Avatar disappears"
  
  cursor_tracking:
    problem: "Live cursor'lar doğru pozisyonda mı?"
    test: "User A moves mouse → User B sees cursor at exact position"
  
  permission_isolation:
    problem: "Kullanıcılar sadece yetkili oldukları yerleri editleyebilmeli"
    test: "Read-only user cannot edit, but sees updates"
```

---

## 📊 Collaboration Patterns

### Pattern 1: Operational Transform (OT)

```yaml
concept: "Transform operations to handle concurrent edits"

example:
  scenario: |
    Initial: "Hello"
    User A: Insert "!" at position 5 → "Hello!"
    User B: Insert " World" at position 5 → "Hello World"
    
    Without OT: Conflict! Data loss
    With OT: Transform B's operation → "Hello World!"

test_cases:
  - Concurrent inserts at same position
  - Concurrent deletes overlapping range
  - Insert + Delete on same area
  - Multiple users editing simultaneously
```

---

### Pattern 2: CRDT (Conflict-free Replicated Data Types)

```yaml
concept: "Mathematically guaranteed convergence"

example:
  scenario: |
    User A offline: Edits document
    User B offline: Edits same document
    Both reconnect: Changes merge automatically

test_cases:
  - Offline editing + merge
  - Network partition
  - Eventual consistency validation
```

---

### Pattern 3: Last-Write-Wins (LWW)

```yaml
concept: "Simplest, but can lose data"

example:
  scenario: |
    User A: Sets color = "red" at 10:00:00
    User B: Sets color = "blue" at 10:00:01
    Result: color = "blue" (last write wins)

test_cases:
  - Timestamp ordering
  - Clock synchronization issues
  - Data loss detection
```

---

## 🔧 Phase 1: Collaboration Scenario Generation

### Multi-User Test Scenarios (Gherkin)

```gherkin
Feature: Real-Time Collaboration
  As multiple users
  We want to work on the same project simultaneously
  So that we can collaborate efficiently

Background:
  Given the collaboration feature is enabled
  And WebSocket connection is established

# ==========================================
# BASIC SYNC TESTS
# ==========================================

Scenario: User sees another user's changes in real-time
  Given User A and User B are in the same project
  When User A adds a "Button" component at position (100, 100)
  Then User B should see the "Button" appear within 200ms
  And the button should be at position (100, 100)
  And User B should see User A's cursor/selection

Scenario: Bidirectional sync
  Given User A and User B are editing
  When User A adds Component X
  And User B adds Component Y
  Then User A should see Component Y
  And User B should see Component X
  And both components should persist

# ==========================================
# PRESENCE AWARENESS
# ==========================================

Scenario: User presence indicators
  Given User A is in the project
  When User B joins the project
  Then User A should see User B's avatar
  And User A should see "User B joined" notification
  When User B leaves the project
  Then User A should see User B's avatar disappear
  And User A should see "User B left" notification

Scenario: Active user list
  Given 5 users are in the project
  When I open the "Active Users" panel
  Then I should see all 5 user avatars
  And each should show their current status (active/idle/away)

Scenario: User cursor tracking
  Given User A and User B are editing
  When User B moves their cursor to position (300, 200)
  Then User A should see User B's cursor at (300, 200)
  And the cursor should show User B's name/color
  And the cursor should follow User B's movements smoothly

# ==========================================
# CONCURRENT EDITING
# ==========================================

Scenario: Concurrent property edits on same component
  Given User A and User B both have Component 1 selected
  When User A changes width to 200
  And User B changes height to 100 (at same time)
  Then Component 1 should have width 200 and height 100
  And no changes should be lost
  And both users should see the final state

Scenario: Concurrent edits on different properties (no conflict)
  Given Component 1 has width: 100, height: 50
  When User A changes width to 200
  And User B changes height to 100 (simultaneously)
  Then Component 1 should have width 200, height 100
  And both changes should apply

Scenario: Concurrent edits on same property (conflict)
  Given Component 1 has color: "red"
  When User A changes color to "blue" at timestamp T1
  And User B changes color to "green" at timestamp T2 (T2 > T1)
  Then Component 1 color should be "green" (last-write-wins)
  Or the system should show conflict resolution UI
  And User A should be notified of conflict

Scenario: Concurrent component additions
  Given an empty canvas
  When User A adds Component X at position (100, 100)
  And User B adds Component Y at position (100, 100) (same position!)
  Then both components should exist
  And the system should auto-adjust positions (snap to grid)
  Or the second component should be slightly offset

# ==========================================
# UNDO/REDO IN COLLABORATION
# ==========================================

Scenario: Undo only own changes
  Given User A added Component X
  And User B added Component Y
  When User A presses Ctrl+Z
  Then only Component X should be undone
  And Component Y should remain (User B's work intact)

Scenario: Redo after undo (collaborative)
  Given User A added and undid Component X
  When User A presses Ctrl+Y
  Then Component X should reappear
  And User B should see Component X reappear

# ==========================================
# CONNECTION RESILIENCE
# ==========================================

Scenario: Graceful disconnect handling
  Given User A is editing
  When User A's internet connection drops
  Then User A should see "Disconnected" indicator
  And User A can continue editing offline
  When connection is restored
  Then User A's offline changes should sync
  And no data should be lost

Scenario: Reconnection after network failure
  Given User A was disconnected for 30 seconds
  And User B made changes during that time
  When User A reconnects
  Then User A should receive all missed changes
  And the canvas should show correct state
  And User A's offline changes should merge

Scenario: Conflict resolution after reconnect
  Given User A was offline and edited Component 1
  And User B edited the same Component 1 while A was offline
  When User A reconnects
  Then the system should detect conflict
  And show conflict resolution UI
  Or apply conflict resolution strategy (OT/CRDT/LWW)
  And notify both users of resolution

# ==========================================
# PERMISSION & ACCESS CONTROL
# ==========================================

Scenario: Read-only user cannot edit
  Given User A has "Editor" role
  And User B has "Viewer" role
  When User B tries to add a component
  Then the action should be prevented
  And User B should see "You don't have edit permission"
  But User B should see User A's changes in real-time

Scenario: Permission change takes effect immediately
  Given User B has "Viewer" role and is viewing project
  When Admin changes User B role to "Editor"
  Then User B should immediately see edit controls
  And User B should be able to add/edit components

# ==========================================
# OPERATIONAL TRANSFORM (OT) TESTS
# ==========================================

Scenario: OT - Concurrent inserts at same position
  Given a text component with content "Hello"
  When User A inserts "!" at position 5
  And User B inserts " World" at position 5 (concurrently)
  Then the final text should be "Hello World!" or "Hello! World"
  And no characters should be lost

Scenario: OT - Insert + Delete conflict
  Given text "Hello World"
  When User A deletes "World" (characters 6-11)
  And User B inserts "Beautiful " before "World" (at position 6)
  Then OT should transform operations correctly
  And the result should be consistent for both users

# ==========================================
# PERFORMANCE TESTS
# ==========================================

Scenario: Sync latency under load
  Given 10 users are editing simultaneously
  When User 1 makes a change
  Then all other 9 users should see the change within 500ms
  And the server should not throttle updates

Scenario: Cursor update performance
  Given 5 users are moving their cursors
  When cursor updates are sent every 50ms
  Then all users should see smooth cursor movements
  And the frame rate should remain > 30 fps

Scenario: Large project sync
  Given a project with 500 components
  When a new user joins
  Then the project should load within 3 seconds
  And all components should be correctly positioned
  And real-time sync should work for all components

# ==========================================
# COMMENTS & ANNOTATIONS
# ==========================================

Scenario: Add comment on component (if feature exists)
  Given User A selects Component 1
  When User A adds comment "Please review this"
  Then User B should see a comment indicator on Component 1
  And clicking it should show "Please review this"
  And User B can reply to the comment

Scenario: Resolve comment
  Given Component 1 has an open comment thread
  When User A marks the comment as "Resolved"
  Then User B should see the comment marked as resolved
  And the comment indicator should update (grayed out)

# ==========================================
# VERSION HISTORY (if applicable)
# ==========================================

Scenario: Auto-save versions
  Given collaborative editing is active
  When significant changes are made
  Then the system should auto-save versions every 5 minutes
  And users can view version history
  And restore previous versions

Scenario: Restore to previous version
  Given version history exists
  When User A restores to version from 1 hour ago
  Then all users should see the project revert
  And current work should be saved as a new version
  And users should be notified of the restore
```

---

## 🔨 Phase 2: Executable Collaboration Tests

### Cypress Multi-User Tests

```javascript
// cypress/e2e/collaboration/real-time-sync.cy.js

describe('Collaboration - Real-Time Sync', () => {
  let userA, userB;

  before(() => {
    // Setup two browser contexts
    cy.task('createBrowserContext', { userId: 'user-a' }).then((ctx) => {
      userA = ctx;
    });
    cy.task('createBrowserContext', { userId: 'user-b' }).then((ctx) => {
      userB = ctx;
    });
  });

  it('should sync changes between users in real-time', () => {
    // User A opens project
    cy.wrap(userA).then((context) => {
      context.visit('/project/123');
      context.waitForWebSocket();
    });

    // User B opens same project
    cy.wrap(userB).then((context) => {
      context.visit('/project/123');
      context.waitForWebSocket();
    });

    // User A adds component
    const startTime = Date.now();
    
    cy.wrap(userA).then((context) => {
      context.addComponentToCanvas('button', { x: 100, y: 100, id: 'btn-1' });
    });

    // User B should see it
    cy.wrap(userB).then((context) => {
      context.get('[data-component-id="btn-1"]', { timeout: 500 })
        .should('exist')
        .and('be.visible');
      
      const syncTime = Date.now() - startTime;
      expect(syncTime).to.be.lessThan(200); // < 200ms
    });
  });

  it('should handle bidirectional sync', () => {
    // User A adds component X
    cy.wrap(userA).then((ctx) => {
      ctx.addComponentToCanvas('button', { id: 'comp-a' });
    });

    // User B adds component Y (simultaneously)
    cy.wrap(userB).then((ctx) => {
      ctx.addComponentToCanvas('input', { id: 'comp-b' });
    });

    // User A should see B's component
    cy.wrap(userA).then((ctx) => {
      ctx.get('[data-component-id="comp-b"]').should('exist');
    });

    // User B should see A's component
    cy.wrap(userB).then((ctx) => {
      ctx.get('[data-component-id="comp-a"]').should('exist');
    });
  });
});

// cypress/e2e/collaboration/presence.cy.js

describe('Collaboration - Presence Awareness', () => {
  it('should show user presence indicators', () => {
    // User A opens project
    cy.loginAs('user-a');
    cy.visit('/project/123');

    // Initially, only User A
    cy.get('[data-test="active-users"]')
      .should('contain', 'You')
      .and('not.contain', 'User B');

    // User B joins
    cy.simulateUserJoin('user-b');

    // User A should see User B
    cy.get('[data-test="active-users"]')
      .should('contain', 'User B');

    cy.get('[data-test="user-avatar"][data-user-id="user-b"]')
      .should('be.visible');

    // Notification should appear
    cy.get('[data-test="notification"]')
      .should('contain', 'User B joined');
  });

  it('should show user cursor tracking', () => {
    cy.loginAs('user-a');
    cy.visit('/project/123');

    // Simulate User B moving cursor
    cy.task('simulateCursorMove', {
      userId: 'user-b',
      position: { x: 300, y: 200 }
    });

    // User A should see User B's cursor
    cy.get('[data-test="remote-cursor"][data-user-id="user-b"]')
      .should('be.visible')
      .and('have.css', 'left', '300px')
      .and('have.css', 'top', '200px');

    // Should show user name
    cy.get('[data-test="remote-cursor"][data-user-id="user-b"]')
      .find('[data-test="cursor-label"]')
      .should('contain', 'User B');
  });
});

// cypress/e2e/collaboration/concurrent-editing.cy.js

describe('Collaboration - Concurrent Editing', () => {
  it('should merge concurrent property changes', () => {
    // Setup: Both users have same component selected
    cy.setupMultiUser(['user-a', 'user-b']);
    
    cy.wrap(userA).then((ctx) => {
      ctx.addComponentToCanvas('button', { id: 'btn-1' });
    });

    // Both select same component
    cy.wrap(userA).then((ctx) => ctx.selectComponent('btn-1'));
    cy.wrap(userB).then((ctx) => ctx.selectComponent('btn-1'));

    // Concurrent edits
    cy.wrap(userA).then((ctx) => {
      ctx.setProperty('width', 200);
    });

    cy.wrap(userB).then((ctx) => {
      ctx.setProperty('height', 100);
    });

    // Both changes should apply
    cy.wrap(userA).then((ctx) => {
      ctx.get('[data-component-id="btn-1"]').should(($btn) => {
        expect($btn.width()).to.equal(200);
        expect($btn.height()).to.equal(100);
      });
    });

    cy.wrap(userB).then((ctx) => {
      ctx.get('[data-component-id="btn-1"]').should(($btn) => {
        expect($btn.width()).to.equal(200);
        expect($btn.height()).to.equal(100);
      });
    });
  });

  it('should handle same property conflict (last-write-wins)', () => {
    cy.setupMultiUser(['user-a', 'user-b']);
    
    cy.wrap(userA).then((ctx) => {
      ctx.addComponentToCanvas('button', { color: 'red', id: 'btn-1' });
    });

    // Concurrent color changes
    cy.wrap(userA).then((ctx) => {
      ctx.setProperty('color', 'blue');
    });

    cy.wait(100); // Small delay

    cy.wrap(userB).then((ctx) => {
      ctx.setProperty('color', 'green');
    });

    // Last write should win (User B's change)
    cy.wrap(userA).then((ctx) => {
      ctx.get('[data-component-id="btn-1"]')
        .should('have.css', 'color', 'green');
    });
  });
});

// cypress/e2e/collaboration/connection-resilience.cy.js

describe('Collaboration - Connection Resilience', () => {
  it('should handle disconnect gracefully', () => {
    cy.loginAs('user-a');
    cy.visit('/project/123');
    cy.waitForWebSocket();

    // Simulate disconnect
    cy.task('disconnectWebSocket', 'user-a');

    // Should show disconnected indicator
    cy.get('[data-test="connection-status"]')
      .should('contain', 'Disconnected')
      .and('have.class', 'status-offline');

    // User can still edit offline
    cy.addComponentToCanvas('button', { id: 'offline-btn' });
    
    // Component should be in local state
    cy.get('[data-component-id="offline-btn"]').should('exist');
  });

  it('should sync offline changes after reconnect', () => {
    cy.loginAs('user-a');
    cy.visit('/project/123');

    // Disconnect
    cy.task('disconnectWebSocket', 'user-a');

    // Make offline changes
    cy.addComponentToCanvas('button', { id: 'offline-btn-1' });
    cy.addComponentToCanvas('input', { id: 'offline-input-1' });

    // Reconnect
    cy.task('reconnectWebSocket', 'user-a');

    cy.get('[data-test="connection-status"]', { timeout: 5000 })
      .should('contain', 'Connected');

    // Changes should sync
    cy.task('verifyComponentExists', {
      projectId: '123',
      componentId: 'offline-btn-1'
    }).should('be.true');

    cy.task('verifyComponentExists', {
      projectId: '123',
      componentId: 'offline-input-1'
    }).should('be.true');
  });

  it('should merge conflicting offline changes', () => {
    // User A goes offline
    cy.wrap(userA).then((ctx) => {
      ctx.disconnect();
      ctx.setProperty('btn-1', 'color', 'blue');
    });

    // User B edits same component while A is offline
    cy.wrap(userB).then((ctx) => {
      ctx.setProperty('btn-1', 'color', 'green');
    });

    // User A reconnects
    cy.wrap(userA).then((ctx) => {
      ctx.reconnect();
    });

    // Conflict resolution should occur
    // (Depends on your strategy: OT, CRDT, or LWW)
    cy.wrap(userA).then((ctx) => {
      // Either shows conflict UI or auto-resolves
      ctx.get('[data-test="conflict-indicator"]')
        .should('exist');
    });
  });
});

// cypress/e2e/collaboration/permissions.cy.js

describe('Collaboration - Permissions', () => {
  it('should prevent read-only user from editing', () => {
    cy.loginAs('viewer-user');
    cy.visit('/project/123');

    // Try to add component
    cy.get('[data-component-type="button"]')
      .trigger('dragstart');

    cy.get('[data-test="canvas"]')
      .trigger('drop');

    // Should be prevented
    cy.get('[data-test="error-message"]')
      .should('contain', "You don't have edit permission");

    // Component should not be added
    cy.get('[data-component]').should('have.length', 0);
  });

  it('should allow viewer to see editor changes', () => {
    // Editor adds component
    cy.task('simulateUserAction', {
      userId: 'editor-user',
      action: 'addComponent',
      data: { type: 'button', id: 'btn-1' }
    });

    // Viewer should see it
    cy.loginAs('viewer-user');
    cy.visit('/project/123');

    cy.get('[data-component-id="btn-1"]')
      .should('exist')
      .and('be.visible');
  });
});
```

---

### WebSocket Test Utilities

```javascript
// cypress/support/collaboration-commands.js

Cypress.Commands.add('waitForWebSocket', (timeout = 5000) => {
  cy.window({ timeout }).should((win) => {
    expect(win.wsConnection).to.exist;
    expect(win.wsConnection.readyState).to.equal(WebSocket.OPEN);
  });
});

Cypress.Commands.add('simulateUserJoin', (userId) => {
  cy.task('broadcastWebSocketMessage', {
    type: 'user:joined',
    data: {
      userId,
      userName: `User ${userId}`,
      avatar: `/avatars/${userId}.png`
    }
  });
});

Cypress.Commands.add('simulateCursorMove', (userId, position) => {
  cy.task('broadcastWebSocketMessage', {
    type: 'cursor:move',
    data: {
      userId,
      x: position.x,
      y: position.y,
      timestamp: Date.now()
    }
  });
});

Cypress.Commands.add('setupMultiUser', (userIds) => {
  const contexts = {};
  
  userIds.forEach((userId) => {
    cy.task('createBrowserContext', { userId }).then((ctx) => {
      contexts[userId] = ctx;
      ctx.visit('/project/123');
      ctx.waitForWebSocket();
    });
  });

  return cy.wrap(contexts);
});

// Backend mock for testing
Cypress.Commands.add('mockWebSocketServer', () => {
  cy.task('startMockWSServer', {
    port: 8080,
    handlers: {
      'component:add': (data) => {
        // Broadcast to all connected clients
        return { type: 'component:added', data };
      },
      'property:update': (data) => {
        return { type: 'property:updated', data };
      },
      'cursor:move': (data) => {
        return { type: 'cursor:moved', data };
      }
    }
  });
});
```

---

### Playwright Multi-Context Tests

```typescript
// tests/collaboration/multi-user.spec.ts

import { test, expect, chromium } from '@playwright/test';

test.describe('Multi-User Collaboration', () => {
  test('should sync changes between two users', async () => {
    // Create two browser contexts (simulate two users)
    const browser = await chromium.launch();
    const contextA = await browser.newContext();
    const contextB = await browser.newContext();

    const pageA = await contextA.newPage();
    const pageB = await contextB.newPage();

    // Both users open same project
    await pageA.goto('/project/123');
    await pageB.goto('/project/123');

    // Wait for WebSocket
    await pageA.waitForSelector('[data-ws-status="connected"]');
    await pageB.waitForSelector('[data-ws-status="connected"]');

    // User A adds component
    await pageA.dragAndDrop(
      '[data-component-type="button"]',
      '[data-test="canvas"]'
    );

    // User B should see it
    await expect(pageB.locator('[data-component-type="button"]'))
      .toBeVisible({ timeout: 500 });

    // User B adds component
    await pageB.dragAndDrop(
      '[data-component-type="input"]',
      '[data-test="canvas"]'
    );

    // User A should see it
    await expect(pageA.locator('[data-component-type="input"]'))
      .toBeVisible({ timeout: 500 });

    await browser.close();
  });

  test('should handle 5 concurrent users', async () => {
    const browser = await chromium.launch();
    const users = [];

    // Create 5 users
    for (let i = 0; i < 5; i++) {
      const context = await browser.newContext();
      const page = await context.newPage();
      await page.goto('/project/123');
      users.push(page);
    }

    // Each user adds a component
    await Promise.all(users.map((page, i) => 
      page.dragAndDrop(
        '[data-component-type="button"]',
        '[data-test="canvas"]',
        { targetPosition: { x: 100 + i * 50, y: 100 } }
      )
    ));

    // Each user should see all 5 components
    for (const page of users) {
      await expect(page.locator('[data-component-type="button"]'))
        .toHaveCount(5);
    }

    await browser.close();
  });
});
```

---

## 📊 Collaboration Test Report

```markdown
# Collaboration Test Report

**Execution Date**: 21 December 2024 16:00:00  
**Total Tests**: 34  
**Duration**: 4m 12s

---

## Summary

| Category | Passed | Failed | Status |
|----------|--------|--------|--------|
| Real-Time Sync | 8 | 0 | ✅ PASS |
| Presence Awareness | 6 | 1 | ⚠️ PARTIAL |
| Concurrent Editing | 5 | 2 | ⚠️ PARTIAL |
| Connection Resilience | 7 | 0 | ✅ PASS |
| Permissions | 4 | 0 | ✅ PASS |
| Operational Transform | 3 | 1 | ⚠️ PARTIAL |
| **TOTAL** | **33** | **4** | **91%** |

---

## Performance Metrics

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Sync Latency (2 users) | < 200ms | 147ms | ✅ |
| Sync Latency (10 users) | < 500ms | 623ms | ❌ |
| Cursor Update Rate | 60 Hz | 58 Hz | ⚠️ |
| Reconnection Time | < 3s | 1.8s | ✅ |
| Message Throughput | 1000 msg/s | 1200 msg/s | ✅ |

---

## Failed Tests (4)

### ❌ 1. Cursor tracking accuracy
**Issue**: Cursor position off by 10-20px  
**Root Cause**: Canvas scroll offset not considered  
**Fix**: Add scroll offset to cursor coordinates

### ❌ 2. OT conflict resolution
**Issue**: Concurrent text edits result in gibberish  
**Root Cause**: OT algorithm not implemented correctly  
**Fix**: Use proven OT library (ShareDB, Yjs)

[... 2 more ...]

---

## Recommendations

### P0 - Critical
1. Fix sync latency for 10+ users (623ms → < 500ms)
2. Implement proper OT algorithm

### P1 - High
1. Improve cursor tracking accuracy
2. Add conflict resolution UI

---

**Collaboration Ready**: ⚠️ Partial (91% tests passing)
```

---

## 🚀 Usage

```markdown
"COLLAB-TEST koduyla collaboration özelliklerini test et.

Özellikler:
- Real-time sync (WebSocket)
- Multi-user editing
- Presence indicators
- Live cursors
- Conflict resolution
- Offline editing + sync

Framework: Cypress + Multi-context

Çıktı:
Phase 1: Multi-user Gherkin scenarios
Phase 2: WebSocket test scripts
Phase 3: Çalıştır ve latency raporu"
```

---

## 📚 Related Modules

- **UI-TEST**: UI interaction testing
- **TEST-GEN**: General test generation
- **PERF**: Performance testing

---

**Collaboration Test Generation Complete** | Multi-User: ✅ | WebSocket: ✅ | Confidence: High (88%)

---

*Module Version: 1.0*  
*Created: December 2024*
