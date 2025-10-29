@echo off
echo Installing Vercel CLI...
call npm install -g vercel

echo.
echo Logging in to Vercel...
call vercel login

echo.
echo Deploying to Vercel...
call vercel --prod

echo.
echo Done! Check your deployment at the URL provided above.
pause

