/**
 * Example: upload, optimize, and transform with Cloudinary.
 * Loads keys from .env (copy .env.example to .env and fill in).
 * Run: node scripts/cloudinary-example.js
 */
const { cloudinary, config, url } = require("../src/config/cloudinary.js");

(async function () {
    if (!config()) {
        console.error(
            "Missing env: CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET. Add them to .env"
        );
        process.exit(1);
    }

    // Example: upload from URL
    const uploadResult = await cloudinary.uploader
        .upload("https://res.cloudinary.com/demo/image/upload/getting-started/shoes.jpg", {
            public_id: "demo-shoes",
        })
        .catch((err) => {
            console.error("Upload error:", err);
            return null;
        });

    if (!uploadResult) process.exit(1);
    console.log("Upload OK:", uploadResult.secure_url);

    // Optimize delivery (auto format + quality)
    const optimizeUrl = url("demo-shoes", { fetch_format: "auto", quality: "auto" });
    console.log("Optimize URL:", optimizeUrl);

    // Transform: resize and auto-crop
    const transformUrl = url("demo-shoes", {
        crop: "auto",
        gravity: "auto",
        width: 500,
        height: 500,
    });
    console.log("Transform URL:", transformUrl);
})();
