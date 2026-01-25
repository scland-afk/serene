# Quick Fix for Cloudflare Pages 404

## Immediate Steps:

### 1. Check Cloudflare Pages Build Settings

Go to your Cloudflare Pages project → **Settings** → **Builds & deployments**

**Required Settings:**
```
Framework preset: None
Build command: npm run build
Build output directory: public
Root directory: / (leave empty)
Node version: 20
```

### 2. Add Environment Variable

In **Settings** → **Environment variables**, add:
```
ELEVENTY_ENV = PROD
```

### 3. Verify Build Command

The build command should be exactly:
```bash
npm run build
```

This runs:
- `npm run build:eleventy` (which sets `ELEVENTY_ENV=PROD` and runs `eleventy`)

### 4. Check Build Logs

1. Go to **Deployments**
2. Click on the failed deployment
3. Check **Build logs** for errors

**Common errors to look for:**
- "Cannot find module" → Missing dependencies
- "SASS compilation error" → Check SASS syntax
- "Template error" → Check Nunjucks syntax

### 5. Test Build Locally First

Before deploying, test locally:

```bash
# Clean install
rm -rf node_modules package-lock.json
npm install

# Build
npm run build

# Verify output
ls public/index.html
```

If `public/index.html` exists, the build works locally.

### 6. Force Rebuild

In Cloudflare Pages:
1. Go to **Deployments**
2. Click **Retry deployment** on the latest build
3. Or push a new commit to trigger a rebuild

### 7. Check File Permissions

Ensure all source files are committed:
```bash
git status
git add .
git commit -m "Fix build configuration"
git push
```

## If Still Getting 404:

The issue might be that the build is completing but not finding `index.html`. 

**Check:**
1. Does `public/index.html` exist after build?
2. Is the build output directory set to `public` (not `dist` or `build`)?
3. Are there any redirect rules interfering?

## Alternative: Manual Upload Test

1. Build locally: `npm run build`
2. Zip the `public/` folder
3. In Cloudflare Pages → **Deployments** → **Create deployment**
4. Upload the zip file
5. If this works, the issue is with the build process, not deployment
