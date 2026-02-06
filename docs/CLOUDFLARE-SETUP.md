# Cloudflare Pages Setup - Step by Step

## ⚠️ IMPORTANT: Fix These Settings First

### 1. Go to Cloudflare Pages Dashboard
- Visit: https://dash.cloudflare.com/
- Navigate to: **Workers & Pages** → **Pages**
- Click on your project: **sass-serene**

### 2. Check Build Settings

Go to **Settings** → **Builds & deployments**

**Verify these exact settings:**

```
Framework preset: None
Build command: npm run build
Build output directory: public
Root directory: / (leave completely empty)
Node version: 20
```

### 3. Add Environment Variable

Go to **Settings** → **Environment variables**

Click **Add variable**:
- **Variable name**: `ELEVENTY_ENV`
- **Value**: `PROD`
- **Environment**: Production (and Preview if you want)

Click **Save**.

### 4. Check Latest Deployment

1. Go to **Deployments** tab
2. Click on the latest deployment
3. Check **Build logs**

**Look for:**
- ✅ "Build completed successfully"
- ❌ Any error messages (copy them)

### 5. Common Issues & Fixes

#### Issue: "Cannot find module"
**Fix:** Ensure `package-lock.json` is committed to GitHub
```bash
git add package-lock.json
git commit -m "Add package-lock.json"
git push
```

#### Issue: "SASS compilation error"
**Fix:** Check for syntax errors in SASS files
- Look at build logs for specific file/line
- Common: Missing semicolons, unclosed brackets

#### Issue: Build succeeds but 404 error
**Fix:** Check build output directory
- Should be exactly: `public`
- Not: `dist`, `build`, `_site`, or anything else

#### Issue: "Command not found: npm"
**Fix:** Set Node version to 20 in build settings

### 6. Force Rebuild

After fixing settings:
1. Go to **Deployments**
2. Click **Retry deployment** on latest build
3. Or push a new commit:
   ```bash
   git commit --allow-empty -m "Trigger rebuild"
   git push
   ```

### 7. Verify Build Output

After a successful build, check:
1. Go to **Deployments** → Latest deployment
2. Click **View build output**
3. You should see:
   - `index.html` (root file)
   - `assets/` folder
   - Other page folders

### 8. Test Locally First

Before deploying, always test locally:

```bash
# Clean install
rm -rf node_modules
npm install

# Build
npm run build

# Check output
ls public/index.html
cat public/index.html | head -20
```

If this works locally but fails on Cloudflare, it's a configuration issue.

## Quick Checklist

- [ ] Build command: `npm run build`
- [ ] Build output: `public`
- [ ] Node version: `20`
- [ ] Environment variable: `ELEVENTY_ENV=PROD`
- [ ] `package-lock.json` is committed
- [ ] Build logs show no errors
- [ ] `public/index.html` exists after build

## Still Not Working?

1. **Check build logs** - They will tell you exactly what's wrong
2. **Try manual upload** - Build locally, zip `public/`, upload to Cloudflare
3. **Check GitHub** - Ensure all files are pushed to the repository
