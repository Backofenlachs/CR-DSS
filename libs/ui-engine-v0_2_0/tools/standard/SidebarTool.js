import { BaseTool } from "../../core/BaseTool.js";

export class SidebarTool extends BaseTool {
    constructor() {
        super()

        this.mountingEngine = null;

        // configs
        this.navItems = null;
    }

    init(config, runtime) {
        super.init(config, runtime);
        console.log("[SidebarTool.init] runtime ", runtime)
        this.mountingEngine = runtime.mountingEngine;

        this.navItems = config?.navItems ?? [
            { label: "Search", toolName: "search" },
            { label: "Risk Assessment", toolName: "risk" }
        ];
    }

    render($root) {
        super.render($root);

        this.$root.html(`
            <div class="sidebar-tool wireframe">
                <nav class="sidebar-tool__nav">
                    <ul class="sidebar-nav">
                        ${this.createNavItemsHtml()}
                    </ul>
                </nav>
            </div>
        `);

        this.bindEvents($root);
    }

    bindEvents($root) {
        $root.on("click", ".sidebar-nav__link", (event) => {
            event.preventDefault();

            const $link = $(event.currentTarget);
            const toolName = $link.data("tool");

            if (!this.mountingEngine) {
                console.warn("SidebarTool: mountingEngine fehlt.");
                return;
            }

            this.mountingEngine.switchTool("content", toolName);
        });
    }

    destroy() {
        this.$root.off("click", ".sidebar-nav__link");
        this.$root.empty();

        this.$root = null;
        this.mountingEngine = null;
        this.navItems = null;
    }

    createNavItemsHtml() {
        return this.navItems.map((item) => `
            <li class="sidebar-nav__item">
                <a href="#" class="sidebar-nav__link" data-tool="${item.toolName}">
                    ${item.label}
                </a>
            </li>
        `).join("");
    }
}