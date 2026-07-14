/*
 * LayoutFactory
 * 
 * Currently the LayoutFactory acts as helper module to build valid LayoutObjects. 
 * that can be translated by the AppShell class.
 * 
 * These helper functions are the first step toward a more formal contract for ShellConfig generation.
 * 
 * The goal is to standadize layout objects and significantly improve their readability.
 * 
 * 
 * Note: This structrue is not final yet. In future, a dedicated Layout class may be introduced as an
 * alternative, espacially for dynamic or runtime layout manipulation.
 * 
 * Note:
 * The optional style field is currently intended as a temporary escape hatch
 * for quick layout prototyping. Regular styling should still be handled via CSS classes.
*/

function validateNonEmptyString(value, name, context) {
    if (typeof value !== "string" || value.trim() === "") {
        throw new Error(`[${context}] Invalid "${name}": expected non-empty string, got ${typeof value}`);
    }
}

function validateStringArray(value, name, context) {
    if (!Array.isArray(value)) {
        throw new Error(`[${context}] Invalid "${name}": expected array of strings, got ${typeof value}`);
    }

    value.forEach((item, index) => {
        if (typeof item !== "string") {
            throw new Error(`[${context}] Invalid item in "${name}" at index ${index}: expected string, got ${typeof item}`);
        }
    });
}

function validateChildren(children, context) {
    if (!Array.isArray(children)) {
        throw new Error (`[LayoutFactory.slot] Invalid "children": expected array, got ${typeof children}`);
    }

    children.forEach((child, index) => {
        if (typeof child !== "object" || child === null) {
            throw new Error(`[${context}] Invalid child at index ${index}: expected object, got ${typeof child}`);
        }
    });
}


export function node(tag="div", classes=[], children=[], style=null) {
    const context = "LayoutFactory.node";

    validateNonEmptyString(tag, "tag", context);
    validateStringArray(classes, "classes", context);
    validateChildren(children, context);

    // --- style reminder ---
    if (style !== null && !Array.isArray(style)) {
        throw new Error(`[LayoutFactory.node] "style" is currently only for fast prototyping. Regular styling should be done via css classes.`);
    }


    return {
        tag: tag,
        classes: classes,
        children: children,
        style: style
    };
}

export function slot(tag="div", slotName, classes=[]) {
    const context = "LayoutFactory.slot";

    validateNonEmptyString(tag, "slot", context);
    validateNonEmptyString(slotName, "slotName", context);
    validateStringArray(classes, "classes", context);
    //alidateChildren(children, context);


    return {
        tag: tag,
        slot: slotName,
        classes: classes,
        children: [],
    };
}