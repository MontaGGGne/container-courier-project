import { SplashScreen, Stack } from "expo-router";
import React from "react";
import { StyleSheet } from "react-native";

SplashScreen.preventAutoHideAsync();

const RootLayout = () => {
  return (
    <Stack>
      <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
      <Stack.Screen name="(auth)" options={{ headerShown: false }} />
      <Stack.Screen name="index" options={{ headerShown: false }} />
    </Stack>
  );
};

export default RootLayout;

const styles = StyleSheet.create({});
