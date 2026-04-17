# Module: UI Interaction Testing (Generic)

**Priority**: P1 (High - Critical for UI Applications)  
**Module Code**: **UI-TEST**  
**Tokens**: ~4500  
**Analysis Time**: 30-45 minutes (Phase 1), 25-35 minutes (Phase 2), 15-25 minutes (Phase 3)  

---

## Purpose

Generic ve framework-agnostic UI testing modülü. Visual builders, design tools, drag-drop uygulamaları, canvas-based interfaces ve herhangi bir interactive UI için E2E testler oluşturur. Property binding, element interaction, visual regression ve responsive behavior'ı doğrular.

**NOT**: Bu modül sadece Visual Builder değil, **Figma-like tools, Excalidraw, Miro, Canva** gibi HERHANGI bir UI uygulaması için kullanılabilir.

---

## 🎯 Çözülen Problemler (Sizin Sorunlarınız)

```yaml
specific_issues:
  property_binding_failure:
    problem: "Property panelindeki değişiklikler canvas'a yansımıyor"
    example: "Width: 200px ayarlıyorum ama element değişmiyor"
    test_scenario: |
      Given a component is selected on canvas
      When I change width to 200px in properties panel
      Then the component on canvas should have width 200px
      And the change should be immediate (< 100ms)
  
  size_control_issues:
    problem: "Ekrana bırakılan nesnelerin boyutları kontrol edilemiyor"
    example: "Button ekledim ama resize handles yok / çalışmıyor"
    test_scenario: |
      Given a button component on canvas
      When I drag the bottom-right resize handle
      Then the button should resize accordingly
      And the new size should be reflected in properties panel
  
  drag_drop_failures:
    problem: "Drag & drop düzgün çalışmıyor"
    example: "Component bazen yanlış yere düşüyor"
    test_scenario: |
      Given I drag a component from sidebar
      When I drop it at coordinates (400, 300)
      Then it should appear exactly at (400, 300)
      And not snap to wrong position
  
  state_synchronization:
    problem: "UI state ve data model senkronize değil"
    example: "Undo yapıyorum ama UI güncellenmiyor"
    test_scenario: |
      Given I have 3 components on canvas
      When I delete one and press Ctrl+Z
      Then the component should reappear on canvas
      And the layers panel should update
      And the properties panel should update

generic_ui_issues:
  interaction_failures:
    - "Click events çalışmıyor"
    - "Keyboard shortcuts tepki vermiyor"
    - "Context menu açılmıyor"
    - "Selection state kaybolıyor"
  
  rendering_issues:
    - "Components yanlış render ediliyor"
    - "Z-index sorunları"
    - "Overflow handling hatalı"
    - "Responsive breakpoints çalışmıyor"
  
  performance_issues:
    - "Yavaş render (> 100 components)"
    - "Memory leaks"
    - "Event listener cleanup eksik"
    - "Re-render loops"
```

---

## 📊 Generic Test Framework

### Test Category Matrix

```yaml
categories:
  1_component_lifecycle:
    - Create (add to canvas)
    - Read (select, inspect)
    - Update (modify properties)
    - Delete (remove from canvas)
  
  2_interaction_types:
    - Click (single, double, right-click)
    - Drag & Drop (component, resize, reorder)
    - Keyboard (shortcuts, text input, navigation)
    - Hover (tooltips, highlights, previews)
    - Scroll (canvas pan, zoom, infinite canvas)
  
  3_property_binding:
    - Visual properties (size, color, position)
    - Layout properties (flex, grid, absolute)
    - Content properties (text, images, data)
    - State properties (visible, locked, selected)
  
  4_state_management:
    - Undo/Redo
    - Save/Load
    - Export/Import
    - History tracking
  
  5_visual_validation:
    - Layout correctness
    - Responsive behavior
    - Accessibility (ARIA, keyboard nav)
    - Cross-browser consistency
  
  6_performance:
    - Render time (< 16ms per frame)
    - Memory usage
    - Event handling latency
    - Large dataset handling (1000+ components)
```

---

## 🔧 Phase 1: UI Analysis & Scenario Generation

### Step 1: UI Component Discovery

```yaml
auto_detection:
  method: "Analyze DOM structure and framework"
  
  detect_framework:
    react: 
      - "data-reactroot"
      - "React DevTools detected"
    vue:
      - "data-v-"
      - "__vue__"
    angular:
      - "ng-"
      - "_ngcontent"
    vanilla:
      - "Custom attributes"
      - "data-* patterns"
  
  detect_patterns:
    canvas_based:
      indicators:
        - "<canvas>" element
        - "fabric.js / konva.js / paper.js"
        - "Custom rendering engine"
      examples: "Figma, Excalidraw, Visual Builder"
    
    dom_based:
      indicators:
        - "Draggable divs"
        - "Absolute positioning"
        - "Transform: translate"
      examples: "Notion, Miro, Trello"
    
    svg_based:
      indicators:
        - "<svg>" elements
        - "D3.js / Raphael.js"
        - "Vector graphics"
      examples: "Diagrams, Charts, Flowcharts"

detect_components:
  action: "Map all interactive UI elements"
  
  component_types:
    containers:
      - "Canvas/Artboard"
      - "Panels (sidebar, properties, layers)"
      - "Modals/Dialogs"
      - "Toolbars"
    
    controls:
      - "Buttons"
      - "Input fields"
      - "Dropdowns"
      - "Sliders"
      - "Color pickers"
    
    canvas_elements:
      - "Shapes (rect, circle, path)"
      - "Text elements"
      - "Images"
      - "Groups/Containers"
      - "Custom components"
    
    interactive_areas:
      - "Drag zones"
      - "Drop zones"
      - "Resize handles"
      - "Rotation handles"
      - "Selection boxes"
```

---

### Step 2: Interaction Pattern Analysis

```yaml
analyze_interactions:
  drag_and_drop:
    patterns:
      - "Sidebar → Canvas (add component)"
      - "Canvas → Canvas (move component)"
      - "Canvas → Trash (delete)"
      - "Layer panel reordering"
    
    validation_points:
      - "Drop coordinates accuracy"
      - "Visual feedback (ghost, highlight)"
      - "State update (model sync)"
      - "Undo/redo support"
  
  property_updates:
    patterns:
      - "Input change → Canvas update"
      - "Slider change → Real-time preview"
      - "Color picker → Style update"
      - "Toggle switch → Visibility change"
    
    validation_points:
      - "Bidirectional binding"
      - "Debouncing (input lag)"
      - "Validation (min/max, format)"
      - "Error handling (invalid input)"
  
  selection_management:
    patterns:
      - "Single select (click)"
      - "Multi-select (Ctrl+click)"
      - "Marquee select (drag rectangle)"
      - "Select all (Ctrl+A)"
    
    validation_points:
      - "Visual indication (highlight, outline)"
      - "Properties panel update"
      - "Context menu availability"
      - "Keyboard navigation"
```

---

### Step 3: Generate Test Scenarios (Gherkin)

```gherkin
Feature: Generic UI Component Management
  As a user of any interactive UI application
  I want to interact with UI elements reliably
  So that my work is saved correctly

# ==========================================
# PROPERTY BINDING TESTS (Your Specific Issue)
# ==========================================

Scenario: Property panel changes reflect on canvas
  Given I have a "Rectangle" component on canvas
  And the component is selected
  When I change "Width" to "200" in properties panel
  Then the canvas component should have width 200px within 100ms
  And the change should be visually apparent
  And the bounding box should update

Scenario: Size input validation
  Given I have a component selected
  When I enter "invalid" in the width field
  Then I should see a validation error
  And the component size should not change
  When I enter "-50" in the width field
  Then I should see "Width must be positive"

Scenario: Real-time property preview
  Given I have a text component selected
  When I start typing in the "Font Size" field
  Then the canvas should update in real-time
  And the preview should be smooth (no lag)
  When I press Enter or blur the field
  Then the change should be committed
  And the undo history should be updated

# ==========================================
# RESIZE & SIZE CONTROL TESTS (Your Specific Issue)
# ==========================================

Scenario: Resize component with handles
  Given I have a "Button" component on canvas
  And the component is selected
  When I hover over the bottom-right resize handle
  Then the cursor should change to "nwse-resize"
  When I drag the handle to increase width by 50px
  Then the button width should increase by 50px
  And the height should remain the same (if aspect ratio not locked)
  And the properties panel should show new width
  And the resize should maintain minimum size constraints

Scenario: Resize maintains constraints
  Given I have a component with min-width: 100px
  When I try to resize it to 50px width
  Then the resize should stop at 100px
  And I should see a visual indicator (snap, highlight)
  
Scenario: Aspect ratio lock
  Given I have an image component
  And aspect ratio is locked
  When I drag the resize handle
  Then both width and height should change proportionally
  And the aspect ratio should remain constant

# ==========================================
# DRAG & DROP TESTS
# ==========================================

Scenario: Add component to canvas via drag-drop
  Given I am on the visual editor page
  And the canvas is visible
  When I drag "Flex Row" from the components panel
  And I drop it at canvas coordinates (400, 300)
  Then a Flex Row component should appear at (400, 300)
  And it should be automatically selected
  And the properties panel should show Flex Row properties
  And the layers panel should show the new component

Scenario: Move component on canvas
  Given I have a component at position (100, 100)
  When I drag the component to position (250, 200)
  Then the component should move smoothly
  And the final position should be exactly (250, 200)
  And the properties panel should reflect the new position
  And the move should be undoable

Scenario: Drag into container (nested drop)
  Given I have a "Flex Row" container on canvas
  When I drag a "Button" component
  And I drop it inside the Flex Row
  Then the Button should become a child of Flex Row
  And the layers panel should show the hierarchy
  And the Button should respect Flex Row layout rules

Scenario: Invalid drop zone
  Given I am dragging a component
  When I hover over an invalid drop zone (e.g., toolbar)
  Then the cursor should show "not-allowed"
  And the drop should be prevented
  When I release the mouse
  Then the component should return to original position

# ==========================================
# SELECTION TESTS
# ==========================================

Scenario: Single component selection
  Given I have 3 components on canvas
  When I click on component 1
  Then only component 1 should be selected
  And component 1 should have a selection highlight
  And the properties panel should show component 1 properties

Scenario: Multi-select with Ctrl+Click
  Given I have 3 components on canvas
  When I click on component 1
  And I hold Ctrl and click on component 2
  Then both components should be selected
  And both should have selection highlights
  And the properties panel should show "Multiple items (2)"

Scenario: Marquee selection
  Given I have 5 components on canvas
  When I start a marquee selection at (100, 100)
  And I drag to (400, 400)
  Then all components within the rectangle should be selected
  And components outside should not be selected
  And I should see the selection rectangle while dragging

Scenario: Deselect all
  Given I have 2 components selected
  When I press Escape
  Then no components should be selected
  And selection highlights should disappear
  When I click on empty canvas area
  Then the same deselection should occur

# ==========================================
# KEYBOARD SHORTCUTS TESTS
# ==========================================

Scenario Outline: Common keyboard shortcuts
  Given I have a component selected
  When I press <shortcut>
  Then <action> should occur

  Examples:
    | shortcut  | action                        |
    | Delete    | Component is deleted          |
    | Ctrl+C    | Component is copied           |
    | Ctrl+V    | Component is pasted           |
    | Ctrl+D    | Component is duplicated       |
    | Ctrl+Z    | Last action is undone         |
    | Ctrl+Y    | Last undo is redone           |
    | Ctrl+A    | All components are selected   |

Scenario: Arrow key nudge
  Given I have a component at position (100, 100)
  When I press the Right arrow key
  Then the component should move to (101, 100)
  When I hold Shift and press Right arrow
  Then the component should move to (111, 100) # 10px jump

# ==========================================
# UNDO/REDO TESTS (State Sync Issue)
# ==========================================

Scenario: Undo component addition
  Given the canvas has 2 components
  When I add a new component
  Then the canvas should have 3 components
  When I press Ctrl+Z
  Then the canvas should have 2 components again
  And the layers panel should update
  And the new component should not be in the DOM

Scenario: Redo after undo
  Given I have performed an action and undone it
  When I press Ctrl+Y
  Then the action should be reapplied
  And the UI should match the pre-undo state

Scenario: Undo property change
  Given I have a component with width 100px
  When I change the width to 200px
  And I press Ctrl+Z
  Then the width should revert to 100px
  And the properties panel should show 100px
  And the canvas should visually reflect 100px

# ==========================================
# SAVE/LOAD TESTS
# ==========================================

Scenario: Save project state
  Given I have created a layout with 5 components
  When I click "Save" button
  Then the project should be saved to localStorage/API
  And I should see a success message
  When I refresh the page
  Then all 5 components should be restored
  And all properties should be intact
  And the undo history should be reset

# ==========================================
# PERFORMANCE TESTS
# ==========================================

Scenario: Handle 100 components smoothly
  Given the canvas is empty
  When I add 100 components programmatically
  Then the rendering should complete in < 2 seconds
  And the UI should remain responsive
  And scrolling should be smooth (60 fps)

Scenario: Property update latency
  Given I have a component selected
  When I change a property value
  Then the canvas should update within 100ms
  And there should be no visual lag

# ==========================================
# RESPONSIVE & VISUAL TESTS
# ==========================================

Scenario: Responsive breakpoints
  Given I have a responsive layout
  When I resize the viewport to mobile width (375px)
  Then the layout should adapt
  And components should reflow correctly
  When I resize to desktop width (1920px)
  Then the layout should expand appropriately

Scenario: Visual regression detection
  Given I have a saved baseline screenshot
  When I render the same layout
  Then the current screenshot should match the baseline
  And pixel differences should be < 1%
```

---

## 🔨 Phase 2: Executable Test Generation

### Cypress Tests (Generic Template)

```javascript
// cypress/e2e/ui-interaction/property-binding.cy.js

describe('UI Interaction - Property Binding', () => {
  beforeEach(() => {
    cy.visit('/'); // Your UI app URL
    cy.waitForCanvasReady(); // Custom command
  });

  describe('Property panel changes reflect on canvas', () => {
    it('should update component width immediately', () => {
      // Given: Rectangle component on canvas
      cy.addComponentToCanvas('rectangle', { x: 400, y: 300, id: 'rect-1' });
      
      // And: Component is selected
      cy.selectComponent('rect-1');

      // When: Change width to 200 in properties panel
      const startTime = Date.now();
      cy.get('[data-test="property-width"]')
        .clear()
        .type('200{enter}');

      // Then: Canvas component should update within 100ms
      cy.get('[data-component-id="rect-1"]').should(($rect) => {
        const updateTime = Date.now() - startTime;
        expect(updateTime).to.be.lessThan(100);
        
        const width = $rect.width();
        expect(width).to.equal(200);
      });

      // And: Bounding box should update
      cy.get('[data-test="selection-box"]')
        .should('have.css', 'width', '200px');
    });

    it('should validate invalid input', () => {
      cy.addComponentToCanvas('button', { id: 'btn-1' });
      cy.selectComponent('btn-1');

      // When: Enter invalid value
      cy.get('[data-test="property-width"]')
        .clear()
        .type('invalid{enter}');

      // Then: Should show error
      cy.get('[data-test="property-error"]')
        .should('be.visible')
        .and('contain', 'Invalid number');

      // And: Component should not change
      cy.get('[data-component-id="btn-1"]')
        .invoke('width')
        .should('not.equal', NaN);
    });

    it('should prevent negative values', () => {
      cy.addComponentToCanvas('button', { id: 'btn-1' });
      cy.selectComponent('btn-1');

      cy.get('[data-test="property-width"]')
        .clear()
        .type('-50{enter}');

      cy.get('[data-test="property-error"]')
        .should('contain', 'must be positive');
    });
  });

  describe('Real-time property preview', () => {
    it('should update canvas while typing (debounced)', () => {
      cy.addComponentToCanvas('text', { id: 'text-1' });
      cy.selectComponent('text-1');

      // Type gradually
      cy.get('[data-test="property-font-size"]')
        .clear()
        .type('2', { delay: 100 });

      // Should update during typing
      cy.get('[data-component-id="text-1"]')
        .should('have.css', 'font-size', '2px');

      cy.get('[data-test="property-font-size"]')
        .type('4', { delay: 100 });

      cy.get('[data-component-id="text-1"]')
        .should('have.css', 'font-size', '24px');
    });
  });
});

// cypress/e2e/ui-interaction/resize.cy.js

describe('UI Interaction - Resize & Size Control', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.waitForCanvasReady();
  });

  describe('Resize component with handles', () => {
    it('should resize using bottom-right handle', () => {
      // Given: Button component
      cy.addComponentToCanvas('button', { 
        x: 100, 
        y: 100, 
        width: 100, 
        height: 40,
        id: 'btn-1'
      });

      cy.selectComponent('btn-1');

      // When: Hover over resize handle
      cy.get('[data-test="resize-handle-br"]') // bottom-right
        .trigger('mouseover');

      // Then: Cursor should change
      cy.get('[data-test="resize-handle-br"]')
        .should('have.css', 'cursor', 'nwse-resize');

      // When: Drag handle +50px width
      cy.get('[data-test="resize-handle-br"]')
        .trigger('mousedown', { button: 0 })
        .trigger('mousemove', { clientX: 250, clientY: 140 }) // +50px
        .trigger('mouseup');

      // Then: Width should increase by 50px
      cy.get('[data-component-id="btn-1"]').should(($btn) => {
        const width = $btn.width();
        expect(width).to.equal(150); // 100 + 50
      });

      // And: Height should remain same (aspect ratio not locked)
      cy.get('[data-component-id="btn-1"]').should(($btn) => {
        const height = $btn.height();
        expect(height).to.equal(40);
      });

      // And: Properties panel should reflect change
      cy.get('[data-test="property-width"]')
        .should('have.value', '150');
    });

    it('should respect minimum size constraints', () => {
      cy.addComponentToCanvas('button', { 
        width: 120, 
        minWidth: 100,
        id: 'btn-1'
      });

      cy.selectComponent('btn-1');

      // Try to resize below minimum
      cy.get('[data-test="resize-handle-br"]')
        .trigger('mousedown')
        .trigger('mousemove', { clientX: 50 }) // Try to make it 50px
        .trigger('mouseup');

      // Should stop at minimum
      cy.get('[data-component-id="btn-1"]')
        .invoke('width')
        .should('be.gte', 100); // >= 100px
    });

    it('should maintain aspect ratio when locked', () => {
      cy.addComponentToCanvas('image', { 
        width: 200, 
        height: 100,
        aspectRatioLocked: true,
        id: 'img-1'
      });

      cy.selectComponent('img-1');

      const originalRatio = 200 / 100; // 2:1

      // Resize width to 300
      cy.get('[data-test="resize-handle-br"]')
        .trigger('mousedown')
        .trigger('mousemove', { clientX: 400 })
        .trigger('mouseup');

      cy.get('[data-component-id="img-1"]').should(($img) => {
        const width = $img.width();
        const height = $img.height();
        const newRatio = width / height;

        expect(newRatio).to.be.closeTo(originalRatio, 0.01);
      });
    });
  });
});

// cypress/e2e/ui-interaction/drag-drop.cy.js

describe('UI Interaction - Drag & Drop', () => {
  describe('Add component via drag-drop', () => {
    it('should add component at exact coordinates', () => {
      const dropX = 400;
      const dropY = 300;

      // Drag from sidebar
      cy.get('[data-component-type="flex-row"]')
        .trigger('dragstart', {
          dataTransfer: new DataTransfer()
        });

      // Drop on canvas
      cy.get('[data-test="canvas"]')
        .trigger('dragover', { clientX: dropX, clientY: dropY })
        .trigger('drop', { 
          clientX: dropX, 
          clientY: dropY,
          dataTransfer: new DataTransfer()
        });

      // Verify position (allowing 5px tolerance for transforms)
      cy.get('[data-component]:last').should(($comp) => {
        const rect = $comp[0].getBoundingClientRect();
        expect(rect.left).to.be.closeTo(dropX, 5);
        expect(rect.top).to.be.closeTo(dropY, 5);
      });

      // Should be selected
      cy.get('[data-component]:last')
        .should('have.class', 'selected');

      // Properties panel should update
      cy.get('[data-test="properties-panel"]')
        .should('contain', 'Flex Row');
    });

    it('should show visual feedback during drag', () => {
      cy.get('[data-component-type="button"]')
        .trigger('dragstart');

      // Should show ghost/preview
      cy.get('[data-test="drag-ghost"]')
        .should('be.visible');

      cy.get('[data-test="canvas"]')
        .trigger('dragover', { clientX: 400, clientY: 300 });

      // Should highlight drop zone
      cy.get('[data-test="canvas"]')
        .should('have.class', 'drop-valid');
    });
  });

  describe('Move component on canvas', () => {
    it('should move to exact position', () => {
      cy.addComponentToCanvas('button', { x: 100, y: 100, id: 'btn-1' });

      // Drag component
      cy.get('[data-component-id="btn-1"]')
        .trigger('mousedown', { clientX: 100, clientY: 100 })
        .trigger('mousemove', { clientX: 250, clientY: 200 })
        .trigger('mouseup');

      // Verify new position
      cy.get('[data-component-id="btn-1"]').should(($btn) => {
        const rect = $btn[0].getBoundingClientRect();
        expect(rect.left).to.be.closeTo(250, 5);
        expect(rect.top).to.be.closeTo(200, 5);
      });

      // Properties should update
      cy.get('[data-test="property-x"]').should('have.value', '250');
      cy.get('[data-test="property-y"]').should('have.value', '200');
    });
  });

  describe('Nested drop (container hierarchy)', () => {
    it('should create parent-child relationship', () => {
      // Add container
      cy.addComponentToCanvas('flex-row', { 
        x: 100, 
        y: 100, 
        width: 300,
        id: 'container-1'
      });

      // Drag button into container
      cy.get('[data-component-type="button"]')
        .trigger('dragstart');

      cy.get('[data-component-id="container-1"]')
        .trigger('dragover', { clientX: 150, clientY: 120 })
        .trigger('drop');

      // Verify hierarchy
      cy.get('[data-component-id="container-1"]')
        .find('[data-component-type="button"]')
        .should('exist');

      // Layers panel should show tree
      cy.get('[data-test="layers-panel"]')
        .find('[data-component-id="container-1"]')
        .find('[data-child]')
        .should('exist');
    });
  });
});

// cypress/e2e/ui-interaction/selection.cy.js

describe('UI Interaction - Selection', () => {
  describe('Multi-select', () => {
    it('should select multiple with Ctrl+Click', () => {
      cy.addComponentToCanvas('button', { id: 'btn-1' });
      cy.addComponentToCanvas('input', { id: 'input-1' });
      cy.addComponentToCanvas('text', { id: 'text-1' });

      // Click first
      cy.get('[data-component-id="btn-1"]').click();
      cy.get('[data-component-id="btn-1"]')
        .should('have.class', 'selected');

      // Ctrl+Click second
      cy.get('[data-component-id="input-1"]')
        .click({ ctrlKey: true });

      // Both should be selected
      cy.get('.selected').should('have.length', 2);

      // Properties should show "Multiple items"
      cy.get('[data-test="properties-panel"]')
        .should('contain', 'Multiple items (2)');
    });
  });

  describe('Marquee selection', () => {
    it('should select all components in rectangle', () => {
      // Create grid of components
      cy.addComponentToCanvas('button', { x: 100, y: 100, id: 'btn-1' });
      cy.addComponentToCanvas('button', { x: 200, y: 100, id: 'btn-2' });
      cy.addComponentToCanvas('button', { x: 100, y: 200, id: 'btn-3' });
      cy.addComponentToCanvas('button', { x: 300, y: 300, id: 'btn-4' }); // Outside

      // Start marquee
      cy.get('[data-test="canvas"]')
        .trigger('mousedown', { clientX: 50, clientY: 50 })
        .trigger('mousemove', { clientX: 250, clientY: 250 });

      // Should show selection rectangle
      cy.get('[data-test="selection-rectangle"]')
        .should('be.visible')
        .and('have.css', 'width', '200px')
        .and('have.css', 'height', '200px');

      // Release
      cy.get('[data-test="canvas"]')
        .trigger('mouseup');

      // First 3 should be selected
      cy.get('.selected').should('have.length', 3);
      cy.get('[data-component-id="btn-4"]')
        .should('not.have.class', 'selected');
    });
  });
});

// cypress/e2e/ui-interaction/undo-redo.cy.js

describe('UI Interaction - Undo/Redo (State Sync)', () => {
  it('should undo component addition', () => {
    // Initial state: 0 components
    cy.get('[data-component]').should('have.length', 0);

    // Add component
    cy.addComponentToCanvas('button', { id: 'btn-1' });
    cy.get('[data-component]').should('have.length', 1);

    // Undo
    cy.get('body').type('{ctrl}z');

    // Should be gone
    cy.get('[data-component]').should('have.length', 0);
    cy.get('[data-component-id="btn-1"]').should('not.exist');

    // Layers panel should update
    cy.get('[data-test="layers-panel"]')
      .find('[data-component]')
      .should('have.length', 0);
  });

  it('should undo property change', () => {
    cy.addComponentToCanvas('button', { 
      width: 100, 
      id: 'btn-1' 
    });

    cy.selectComponent('btn-1');

    // Change width
    cy.get('[data-test="property-width"]')
      .clear()
      .type('200{enter}');

    cy.get('[data-component-id="btn-1"]')
      .invoke('width')
      .should('equal', 200);

    // Undo
    cy.get('body').type('{ctrl}z');

    // Should revert
    cy.get('[data-component-id="btn-1"]')
      .invoke('width')
      .should('equal', 100);

    // Properties panel should update
    cy.get('[data-test="property-width"]')
      .should('have.value', '100');
  });

  it('should redo after undo', () => {
    cy.addComponentToCanvas('button', { id: 'btn-1' });

    // Undo
    cy.get('body').type('{ctrl}z');
    cy.get('[data-component]').should('have.length', 0);

    // Redo
    cy.get('body').type('{ctrl}y');
    cy.get('[data-component]').should('have.length', 1);
    cy.get('[data-component-id="btn-1"]').should('exist');
  });
});
```

---

### Playwright Tests (Alternative)

```typescript
// tests/ui-interaction/property-binding.spec.ts

import { test, expect } from '@playwright/test';

test.describe('Property Binding', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('[data-test="canvas"]');
  });

  test('property changes reflect on canvas immediately', async ({ page }) => {
    // Add component
    await page.dragAndDrop(
      '[data-component-type="rectangle"]',
      '[data-test="canvas"]',
      { targetPosition: { x: 400, y: 300 } }
    );

    // Select component
    await page.click('[data-component]:last-child');

    // Change width
    const startTime = Date.now();
    await page.fill('[data-test="property-width"]', '200');
    await page.press('[data-test="property-width"]', 'Enter');

    // Verify update time
    const updateTime = Date.now() - startTime;
    expect(updateTime).toBeLessThan(100);

    // Verify width
    const component = await page.locator('[data-component]:last-child');
    const box = await component.boundingBox();
    expect(box?.width).toBeCloseTo(200, 1);
  });

  test('validates numeric input', async ({ page }) => {
    await page.dragAndDrop('[data-component-type="button"]', '[data-test="canvas"]');
    await page.click('[data-component]:last-child');

    // Invalid input
    await page.fill('[data-test="property-width"]', 'abc');
    await page.press('[data-test="property-width"]', 'Enter');

    // Error should appear
    await expect(page.locator('[data-test="property-error"]'))
      .toContainText('Invalid number');
  });
});

test.describe('Resize Handles', () => {
  test('resizes component with bottom-right handle', async ({ page }) => {
    await page.goto('/');
    
    // Add button
    const button = await page.dragAndDrop(
      '[data-component-type="button"]',
      '[data-test="canvas"]'
    );

    await page.click('[data-component]:last-child');

    // Get initial width
    const initialBox = await page.locator('[data-component]:last-child').boundingBox();
    const initialWidth = initialBox!.width;

    // Resize
    await page.hover('[data-test="resize-handle-br"]');
    
    // Verify cursor
    const cursor = await page.evaluate(() => {
      const handle = document.querySelector('[data-test="resize-handle-br"]');
      return window.getComputedStyle(handle!).cursor;
    });
    expect(cursor).toBe('nwse-resize');

    // Drag +50px
    await page.mouse.move(initialBox!.x + initialBox!.width, initialBox!.y + initialBox!.height);
    await page.mouse.down();
    await page.mouse.move(initialBox!.x + initialBox!.width + 50, initialBox!.y + initialBox!.height);
    await page.mouse.up();

    // Verify new width
    const newBox = await page.locator('[data-component]:last-child').boundingBox();
    expect(newBox!.width).toBeCloseTo(initialWidth + 50, 5);

    // Properties panel should update
    const widthInput = await page.locator('[data-test="property-width"]');
    await expect(widthInput).toHaveValue(String(Math.round(newBox!.width)));
  });
});
```

---

## 📊 Phase 3: Execution & Reporting

### Custom Commands (Cypress)

```javascript
// cypress/support/commands.js

// Generic UI test utilities
Cypress.Commands.add('waitForCanvasReady', (timeout = 5000) => {
  cy.get('[data-test="canvas"]', { timeout })
    .should('be.visible')
    .and('not.have.class', 'loading');
});

Cypress.Commands.add('addComponentToCanvas', (type, options = {}) => {
  const { x = 400, y = 300, id, ...props } = options;

  // Drag from sidebar
  cy.get(`[data-component-type="${type}"]`)
    .trigger('dragstart', { dataTransfer: new DataTransfer() });

  // Drop on canvas
  cy.get('[data-test="canvas"]')
    .trigger('drop', {
      clientX: x,
      clientY: y,
      dataTransfer: new DataTransfer()
    });

  // Set custom ID if provided
  if (id) {
    cy.get('[data-component]:last').invoke('attr', 'data-component-id', id);
  }

  // Set additional properties
  if (Object.keys(props).length > 0) {
    cy.selectComponent(id || '[data-component]:last');
    Object.entries(props).forEach(([key, value]) => {
      cy.get(`[data-test="property-${key}"]`).clear().type(String(value));
    });
  }
});

Cypress.Commands.add('selectComponent', (identifier) => {
  const selector = identifier.startsWith('[') 
    ? identifier 
    : `[data-component-id="${identifier}"]`;
  
  cy.get(selector).click();
});

Cypress.Commands.add('resizeComponent', (identifier, direction, delta) => {
  cy.selectComponent(identifier);
  
  const handle = cy.get(`[data-test="resize-handle-${direction}"]`);
  
  handle
    .trigger('mousedown')
    .trigger('mousemove', { clientX: delta.x, clientY: delta.y })
    .trigger('mouseup');
});

Cypress.Commands.add('verifyComponentProperty', (identifier, property, expectedValue) => {
  cy.selectComponent(identifier);
  
  cy.get(`[data-test="property-${property}"]`)
    .should('have.value', String(expectedValue));
});

// Visual regression
Cypress.Commands.add('matchesBaseline', (name, options = {}) => {
  cy.screenshot(name, options);
  
  // Compare with baseline (requires plugin)
  cy.task('compareScreenshot', {
    name,
    threshold: options.threshold || 0.01
  });
});
```

---

## 🎨 Generic Application Adapters

To make this work with **ANY** UI application, create an adapter:

```javascript
// cypress/support/adapters/visual-builder-adapter.js

export const VisualBuilderAdapter = {
  selectors: {
    canvas: '[data-test="canvas"]',
    component: '[data-component]',
    componentType: (type) => `[data-component-type="${type}"]`,
    propertiesPanel: '[data-test="properties-panel"]',
    property: (name) => `[data-test="property-${name}"]`,
    layersPanel: '[data-test="layers-panel"]',
    resizeHandle: (direction) => `[data-test="resize-handle-${direction}"]`,
  },

  actions: {
    addComponent(type, position) {
      cy.get(this.selectors.componentType(type))
        .trigger('dragstart');
      cy.get(this.selectors.canvas)
        .trigger('drop', { clientX: position.x, clientY: position.y });
    },

    selectComponent(id) {
      cy.get(`[data-component-id="${id}"]`).click();
    },

    setProperty(name, value) {
      cy.get(this.selectors.property(name)).clear().type(String(value));
    },

    resize(component, handle, delta) {
      cy.get(component)
        .find(this.selectors.resizeHandle(handle))
        .trigger('mousedown')
        .trigger('mousemove', delta)
        .trigger('mouseup');
    }
  },

  assertions: {
    componentExists(id) {
      cy.get(`[data-component-id="${id}"]`).should('exist');
    },

    propertyEquals(name, value) {
      cy.get(this.selectors.property(name))
        .should('have.value', String(value));
    },

    componentHasSize(id, width, height) {
      cy.get(`[data-component-id="${id}"]`).should(($el) => {
        const box = $el[0].getBoundingClientRect();
        expect(box.width).to.be.closeTo(width, 5);
        expect(box.height).to.be.closeTo(height, 5);
      });
    }
  }
};

// Usage:
import { VisualBuilderAdapter as adapter } from './adapters/visual-builder-adapter';

adapter.actions.addComponent('button', { x: 400, y: 300 });
adapter.actions.setProperty('width', 200);
adapter.assertions.propertyEquals('width', 200);
```

---

### Adapter for Other UI Tools

```javascript
// Figma-like adapter
export const FigmaAdapter = {
  selectors: {
    canvas: '.figma-canvas',
    component: '.figma-node',
    // ...
  }
};

// Miro-like adapter
export const MiroAdapter = {
  selectors: {
    canvas: '.board-container',
    component: '.board-item',
    // ...
  }
};

// Excalidraw adapter
export const ExcalidrawAdapter = {
  selectors: {
    canvas: 'canvas.excalidraw',
    component: '.excalidraw-element',
    // ...
  }
};
```

---

## 📋 Test Execution Report Template

```markdown
# UI Interaction Test Report

**Application**: Visual Builder  
**Execution Date**: 21 December 2024 15:30:00  
**Framework**: Cypress 13.6.0  
**Total Tests**: 87  
**Duration**: 3m 24s

---

## Summary

| Category | Passed | Failed | Skipped | Coverage |
|----------|--------|--------|---------|----------|
| Property Binding | 12 | 3 | 0 | 80% |
| Resize & Size Control | 8 | 2 | 0 | 80% |
| Drag & Drop | 15 | 1 | 0 | 93% |
| Selection | 11 | 0 | 0 | 100% |
| Keyboard Shortcuts | 9 | 0 | 0 | 100% |
| Undo/Redo | 7 | 1 | 0 | 85% |
| Performance | 5 | 0 | 0 | 100% |
| **TOTAL** | **67** | **7** | **0** | **91%** |

---

## Failed Tests (7) - YOUR ISSUES DETECTED! 🔍

### ❌ 1. Property width change not reflecting (CRITICAL)
**File**: `property-binding.cy.js:15`  
**Issue**: Width property change doesn't update canvas  
**Error**:
```
AssertionError: expected 100 to equal 200
  at property-binding.cy.js:25
```

**Root Cause**: Property binding broken  
**Location**: `src/components/PropertiesPanel.tsx:145`  
**Fix**: 
```typescript
// Current (broken):
onChange={(value) => console.log(value)} // ❌ Only logging!

// Should be:
onChange={(value) => updateComponent(selectedId, { width: value })} // ✅
```

**Priority**: P0 - CRITICAL  
**Estimated Fix Time**: 15 minutes

---

### ❌ 2. Resize handle not working (CRITICAL)
**File**: `resize.cy.js:45`  
**Issue**: Dragging resize handle doesn't change component size  
**Error**:
```
Expected component width to increase, but remained 100px
```

**Root Cause**: Missing event listener on resize handle  
**Location**: `src/components/Canvas/ResizeHandles.tsx:78`  
**Fix**:
```typescript
// Add missing event listeners:
<div 
  className="resize-handle-br"
  onMouseDown={handleResizeStart}  // ✅ Add this
  onMouseMove={handleResizeMove}   // ✅ Add this
  onMouseUp={handleResizeEnd}      // ✅ Add this
/>
```

**Priority**: P0 - CRITICAL  
**Estimated Fix Time**: 30 minutes

---

### ❌ 3. Drop position inaccurate
**File**: `drag-drop.cy.js:89`  
**Issue**: Component drops at wrong coordinates  
**Error**:
```
Expected position (400, 300), got (356, 287)
```

**Root Cause**: Canvas scroll offset not accounted for  
**Location**: `src/components/Canvas/Canvas.tsx:234`  
**Fix**:
```typescript
// Current (broken):
const x = event.clientX;
const y = event.clientY;

// Should be:
const rect = canvasRef.current.getBoundingClientRect();
const x = event.clientX - rect.left + canvasRef.current.scrollLeft;
const y = event.clientY - rect.top + canvasRef.current.scrollTop;
```

**Priority**: P1 - High  
**Estimated Fix Time**: 20 minutes

---

[... 4 more failures ...]

---

## Performance Metrics

| Test | Metric | Target | Actual | Status |
|------|--------|--------|--------|--------|
| Property Update | Latency | < 100ms | 87ms | ✅ PASS |
| Render 100 Components | Time | < 2s | 1.4s | ✅ PASS |
| Drag Smoothness | FPS | 60 fps | 58 fps | ⚠️ CLOSE |
| Memory Usage (1000 comp) | Heap | < 100MB | 78MB | ✅ PASS |

---

## Recommendations

### Priority 0 (Fix Immediately)
1. ✅ Fix property binding in PropertiesPanel
2. ✅ Add resize handle event listeners
3. ✅ Fix drop position calculation

### Priority 1 (Fix This Sprint)
1. Improve undo/redo state synchronization
2. Add input validation for negative values
3. Fix multi-select Ctrl+Click on Firefox

### Priority 2 (Nice to Have)
1. Optimize drag performance (58 fps → 60 fps)
2. Add visual feedback during property updates
3. Implement keyboard shortcuts for resize

---

## Coverage Report

**Line Coverage**: 78.5%  
**Branch Coverage**: 65.2%  
**Function Coverage**: 82.1%

**Well-Tested**:
- ✅ Selection management (100%)
- ✅ Keyboard shortcuts (100%)
- ✅ Performance (100%)

**Needs Attention**:
- ⚠️ Property binding (60%)
- ⚠️ Resize handlers (45%)
- ❌ Nested drag-drop (30%)

---

**Total Issues Found**: 7  
**Critical Issues**: 3  
**High Priority**: 2  
**Medium Priority**: 2

**Next Steps**:
1. Fix 3 critical issues (estimated 1.25 hours)
2. Re-run tests to verify fixes
3. Add missing test coverage for nested drag-drop
```

---

## 🚀 Usage

### Generate Tests for Your Visual Builder

```markdown
"UI-TEST koduyla visual builder testlerini oluştur.

Uygulama: Visual Builder (ekran görüntüsündeki)

Test edilecek özellikler:
- Property panel → Canvas binding (ÇOK ÖNEMLİ - ÇALIŞMIYOR!)
- Resize handles (boyut kontrolü - ÇOK ÖNEMLİ - ÇALIŞMIYOR!)
- Drag & drop (sidebar → canvas)
- Component selection (tek, çoklu, marquee)
- Undo/Redo state sync
- Keyboard shortcuts
- Save/Load

Framework: Cypress

Çıktı:
Phase 1: Gherkin scenarios (Türkçe açıklamalar)
Phase 2: Cypress executable tests
Phase 3: Çalıştır ve rapor oluştur

Özellikle property binding ve resize handle sorunlarını tespit et!"
```

---

## 📚 Related Modules

- **TEST-GEN**: Unit/integration tests
- **COLLAB-TEST**: Multi-user testing (separate module)
- **PERF**: Performance testing
- **A11Y**: Accessibility testing

---

**UI Test Generation Complete** | Tests: 87 | Issues Found: 7 | Confidence: High (92%)

---

*Module Version: 1.0*  
*Created: December 2024*  
*Generic & Reusable for Any UI Application*
