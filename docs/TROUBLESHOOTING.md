# Troubleshooting Cloudflare Pages 404 Error

## Common Causes & Solutions

### 1. Check Build Logs in Cloudflare Dashboard

1. Go to your Cloudflare Pages project
2. Click on **Deployments**
3. Click on the latest deployment
4. Check the **Build logs** for errors

### 2. Verify Build Settings

In Cloudflare Pages settings, ensure:
- **Build command**: `npm run build`
- **Build output directory**: `public`
- **Root directory**: `/` (leave empty)
- **Node version**: `20` (or `18`)

### 3. Environment Variables

Add this environment variable in Cloudflare Pages:
- **Variable name**: `ELEVENTY_ENV`
- **Value**: `PROD`

### 4. Test Build Locally

Run these commands to verify the build works:

```bash
# Install dependencies
npm install

# Build the site
npm run build

# Check if public/index.html exists
ls public/index.html
```

If `public/index.html` doesn't exist, the build failed.

### 5. Common Build Issues

**Issue: Missing dependencies**
```bash
# Solution: Ensure package-lock.json is committed
git add package-lock.json
git commit -m "Add package-lock.json"
git push
```

**Issue: Build timeout**
- Cloudflare Pages has a 20-minute build limit
- If your build takes longer, optimize images or reduce build steps

**Issue: Node version mismatch**
- Ensure `.nvmrc` specifies Node 20
- Or set Node version to 20 in Cloudflare Pages settings

### 6. Verify File Structure

After building locally, check that `public/` contains:
- `index.html` (root file)
- `assets/` folder
- Other page folders

### 7. Check for Build Errors

Common errors:
- **SASS compilation errors**: Check `src/assets/sass/` for syntax errors
- **Missing images**: Ensure all image paths are correct
- **Template errors**: Check Nunjucks syntax in templates

### 8. Manual Deployment Test

If automatic deployment fails:
1. Build locally: `npm run build`
2. In Cloudflare Pages, go to **Deployments** → **Create deployment**
3. Upload the `public/` folder as a zip file
4. This will help identify if it's a build issue or deployment issue

### 9. Check _redirects File

Ensure `src/_redirects` exists and is being copied to `public/`. This file helps with routing.

### 10. Clear Cache

After fixing issues:
1. In Cloudflare Pages, go to **Settings** → **Builds & deployments**
2. Clear build cache
3. Trigger a new deployment

## Still Not Working?

1. Check Cloudflare Pages build logs for specific error messages
2. Verify all files are committed to GitHub
3. Ensure `package.json` and `package-lock.json` are in the repository
4. Try building with a fresh clone of the repository
