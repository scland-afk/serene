# Quick Fix for 404 Error on Cloudflare Pages

## 🔴 Most Common Issue: Build Settings

### Step 1: Check Cloudflare Pages Settings

1. Go to: https://dash.cloudflare.com/ → **Workers & Pages** → **Pages** → Your Project
2. Click **Settings** → **Builds & deployments**
3. Verify these **EXACT** settings:

```
Framework preset: None
Build command: npm run build
Build output directory: public
Root directory: (leave completely empty - not "/")
Node version: 20
```

### Step 2: Add Environment Variable

1. Still in **Settings**, go to **Environment variables**
2. Click **Add variable**
3. Add:
   - **Variable name**: `ELEVENTY_ENV`
   - **Value**: `PROD`
   - **Environment**: Production
4. Click **Save**

### Step 3: Check Build Logs

1. Go to **Deployments** tab
2. Click on the latest deployment
3. Scroll to **Build logs**
4. Look for errors (they'll be in red)

**Common errors:**
- ❌ "Cannot find module" → Missing dependencies
- ❌ "SASS error" → Syntax error in SASS file
- ❌ "Template error" → Nunjucks syntax issue

### Step 4: Retry Build

After fixing settings:
1. Go to **Deployments**
2. Click **Retry deployment** on the latest build
3. Wait for it to complete
4. Check if the site loads

## ✅ Verify Build Works Locally

Before deploying, test locally:

```bash
# Install dependencies
npm install

# Build the site
npm run build

# Check if index.html was created
ls public/index.html
```

If `public/index.html` exists, the build works!

## 🔧 If Build Fails

### Check These Files Are Committed:

```bash
git status
```

Make sure these are committed:
- ✅ `package.json`
- ✅ `package-lock.json`
- ✅ `.eleventy.js`
- ✅ All files in `src/`

### Common Fixes:

1. **Missing package-lock.json**
   ```bash
   npm install
   git add package-lock.json
   git commit -m "Add package-lock.json"
   git push
   ```

2. **SASS Error**
   - Check build logs for the specific file/line
   - Common: Missing semicolon, unclosed bracket

3. **Node Version**
   - Set to exactly `20` in Cloudflare settings
   - Or use `.nvmrc` file (already created)

## 📋 Checklist

Before asking for help, verify:
- [ ] Build command: `npm run build`
- [ ] Output directory: `public` (not `dist` or `build`)
- [ ] Environment variable: `ELEVENTY_ENV=PROD` added
- [ ] Node version: `20` set
- [ ] `package-lock.json` is committed
- [ ] Build logs show no errors
- [ ] Local build works (`npm run build`)

## 🆘 Still Not Working?

1. **Share build logs** - Copy the error from Cloudflare build logs
2. **Test locally first** - If local build fails, fix that first
3. **Check file structure** - Ensure `src/index.html` exists
