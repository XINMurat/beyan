# Module: Mobile Native Analysis

**Priority**: P2
**Tokens**: ~2000
**Analysis Time**: Loaded when pubspec.yaml, Podfile, or android/ detected

---

## Purpose
Analyzes React Native, Flutter, or native iOS/Android projects for platform-specific performance issues, App Store compliance, and mobile UX best practices.

---

## Flutter Analysis

```yaml
flutter_checks:
  const_constructors:
    check: "const Text(), const Icon() used wherever possible to prevent unnecessary rebuilds"
  state_management:
    check: "setState() rebuilds entire widget tree — large apps should use Riverpod/Bloc/Provider"
  platform_channels:
    check: "MethodChannel bridges have proper error handling?"
```

## React Native Analysis

```yaml
rn_checks:
  architecture:
    check: "New Architecture (JSI/Fabric) or old Bridge? New Arch removes serialization overhead."
  flatlist:
    check: "getItemLayout, keyExtractor, initialNumToRender, windowSize optimized?"
  hermes:
    check: "Hermes JS engine enabled? Significantly improves startup time."
```

## App Store Requirements

```yaml
ios_app_store:
  - "Privacy Manifest (PrivacyInfo.xcprivacy) required for iOS 17+"
  - "App Transport Security (ATS) — HTTP exceptions must be justified"
  - "64-bit binary support required"
google_play:
  - "targetSdkVersion at latest Android API level?"
  - "64-bit native libraries included?"
  - "Data Safety section completed in Play Console?"
```

## Scoring

```yaml
scoring:
  excellent: "const constructors everywhere, New Architecture, all App Store requirements met."
  good: "Generally optimized, minor rebuild issues, compliance mostly met."
  attention: "Heavy setState usage, old Bridge, Privacy Manifest missing."
  critical: "No performance optimization, App Store rejection risk."
```
