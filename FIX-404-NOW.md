# 🔴 FIX 404 ERROR - Step by Step

## The Problem
Your Cloudflare Pages site shows 404 because the build either:
1. Failed (check build logs)
2. Built to wrong directory
3. Missing environment variable

## ✅ SOLUTION - Do These Steps:

### Step 1: Check Cloudflare Pages Build Settings

1. Go to: https://dash.cloudflare.com/
2. Navigate to: **Workers & Pages** → **Pages** → **sass-serene**
3. Click: **Settings** → **Builds & deployments**

**Set these EXACT values:**

| Setting | Value |
|--------|-------|
| Framework preset | **None** |
| Build command | `npm run build` |
| Build output directory | `public` |
| Root directory | **(leave completely empty)** |
| Node version | `20` |

### Step 2: Add Environment Variable (CRITICAL!)

1. Still in **Settings**, scroll to **Environment variables**
2. Click **Add variable**
3. Enter:
   - **Variable name**: `ELEVENTY_ENV`
   - **Value**: `PROD`
   - **Environment**: Select **Production** (and **Preview** if you want)
4. Click **Save**

### Step 3: Check Build Logs

1. Go to **Deployments** tab
2. Click on the **latest deployment**
3. Scroll down to **Build logs**
4. **Look for errors** (they'll be in red)

**What to look for:**
- ✅ "Build completed successfully" = Good!
- ❌ Any red error messages = Problem (copy the error)

### Step 4: Retry Build

1. In **Deployments**, click **Retry deployment** on the latest build
2. Wait 2-3 minutes
3. Check if site loads

## 🧪 Test Build Locally First

Before deploying, verify it works:

```bash
# In your project folder
npm install
npm run build

# Check if index.html was created
ls public/index.html
```

If `public/index.html` exists, the build works!

## ❌ Common Errors & Fixes

### Error: "Cannot find module"
**Fix:** Ensure `package-lock.json` is committed
```bash
git add package-lock.json
git commit -m "Add package-lock.json"
git push
```

### Error: "SASS compilation error"
**Fix:** Check the specific file mentioned in error
- Look for missing semicolons `;`
- Check for unclosed brackets `{ }`

### Error: Build succeeds but still 404
**Fix:** Verify build output directory is exactly `public` (not `dist` or `build`)

### Error: "Command not found: npm"
**Fix:** Set Node version to `20` in build settings

## 📋 Quick Checklist

Before asking for help, verify ALL of these:

- [ ] Build command: `npm run build` (exactly this)
- [ ] Build output directory: `public` (exactly this, lowercase)
- [ ] Root directory: Empty (not "/" or anything else)
- [ ] Node version: `20`
- [ ] Environment variable `ELEVENTY_ENV=PROD` is added
- [ ] `package-lock.json` is committed to GitHub
- [ ] Build logs show no errors
- [ ] Local build works (`npm run build` creates `public/index.html`)

## 🆘 Still Not Working?

1. **Copy the exact error** from Cloudflare build logs
2. **Share the error message** - it will tell us exactly what's wrong
3. **Check if local build works** - if local fails, fix that first

## 📞 What to Share for Help

If you need help, provide:
1. Screenshot of Cloudflare build settings
2. Copy of build logs (especially any errors)
3. Result of `npm run build` when run locally
