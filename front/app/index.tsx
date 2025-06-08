import { router } from "expo-router";
import React, { useState } from "react";
import {
  ActivityIndicator,
  Pressable,
  StyleSheet,
  Text,
  View,
} from "react-native";
import styled from "styled-components/native";

const BgView = styled.View`
  flex: 1;
  justify-content: center;
  align-items: center;
`;

const BackgroundImage = styled.ImageBackground`
  flex: 1;
  width: 100%;
  height: 100%;
  justify-content: center;
  align-items: center;
`;

export default function App() {
  const [loading, setLoading] = useState(false);

  const checkServerConnection = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/test");
      if (response.ok) {
        setLoading(false);
        router.push("/sign-in");
      } else {
        setTimeout(checkServerConnection, 5000);
      }
    } catch (error) {
      setTimeout(checkServerConnection, 5000);
    }
  };

  const handlePress = () => {
    checkServerConnection();
  };

  //   useEffect(() => {
  //     checkServerConnection();
  //   }, []);

  return (
    <Pressable style={{ flex: 1 }} onPress={handlePress}>
      <BgView>
        <BackgroundImage
          source={require("../assets/images/homload.jpg")}
          resizeMode="cover"
          style={{ alignItems: "flex-end", justifyContent: "flex-end" }}
        >
          <View style={styles.containerText}>
            <Text style={styles.homeTitle}>Блинбери</Text>
            <Text style={styles.homeSubText}>v1.0</Text>
          </View>
          {loading && (
            <View style={styles.load}>
              <ActivityIndicator size="large" color="white" />
            </View>
          )}
        </BackgroundImage>
      </BgView>
    </Pressable>
  );
}

const styles = StyleSheet.create({
  load: {
    position: "absolute",
    bottom: 20,
    width: "100%",
    justifyContent: "center",
    alignItems: "center",
  },
  containerText: {
    width: "80%",
    height: "60%",
    backgroundColor: "rgba(0, 0, 0, 0.5)",
    justifyContent: "flex-start",
    alignItems: "flex-start",
    paddingHorizontal: 30,
    paddingVertical: 30,
  },
  homeTitle: {
    color: "white",
    fontSize: 50,
    fontWeight: "bold",
    textAlign: "center",
  },
  homeSubText: {
    color: "white",
    fontSize: 20,
    fontWeight: "bold",
    textAlign: "center",
  },
});
