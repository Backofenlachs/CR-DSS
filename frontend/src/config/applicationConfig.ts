import type {
    CRDSSHeaderConfig
} from "../tools/CRDSSHeaderTool.js";

/**
 * Temporary static metadata for CR-DSS UI v0.1.0.
 *
 * Later sources:
 * - UI version: frontend build/application configuration
 * - Server version: backend system metadata endpoint
 * - Risk Engine version: backend system metadata endpoint
 */
export const HEADER_CONFIG: CRDSSHeaderConfig = {
    title: "CR-DSS",
    subtitle: "Credit Risk Decision Support System",

    versions: {
        riskEngine: "0.2.0",
        server: "0.1.0",
        ui: "0.1.0"
    }
};