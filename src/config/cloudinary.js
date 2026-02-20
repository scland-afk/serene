/**
 * Cloudinary config and helpers.
 * Loads .env from project root. Set there (never commit .env):
 *   CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET
 */
require("dotenv").config({ path: require("path").resolve(__dirname, "../../.env") });
const { v2: cloudinary } = require("cloudinary");

function config() {
    const cloud_name = process.env.CLOUDINARY_CLOUD_NAME;
    const api_key = process.env.CLOUDINARY_API_KEY;
    const api_secret = process.env.CLOUDINARY_API_SECRET;

    if (cloud_name && api_key && api_secret) {
        cloudinary.config({
            cloud_name,
            api_key,
            api_secret,
        });
        return true;
    }
    return false;
}

/**
 * Get a Cloudinary URL for an existing image (by public_id).
 * Options: width, height, crop, fetch_format, quality, etc.
 * @see https://cloudinary.com/documentation/image_transformations
 */
function url(publicId, options = {}) {
    const defaults = {
        fetch_format: "auto",
        quality: "auto",
        secure: true,
    };
    return cloudinary.url(publicId, { ...defaults, ...options });
}

module.exports = {
    cloudinary,
    config,
    url,
};
