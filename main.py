name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    container:
      image: kivy/buildozer
    steps:
      - uses: actions/checkout@v4
      - name: Build with Buildozer
        run: |
          buildozer android debug
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: app-apk
          path: bin/*.apk
