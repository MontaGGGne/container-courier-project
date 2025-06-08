import AsyncStorage from "@react-native-async-storage/async-storage";
import { router } from "expo-router";
import React, { useState } from "react";
import {
  Alert,
  Pressable,
  StyleSheet,
  Text,
  TextInput,
  View,
} from "react-native";

const AuthLayout = () => {
  const [email, setEmail] = useState("");

  const handleSubmit = async () => {
    if (email.trim() === "") {
      Alert.alert("Ошибка", "Пожалуйста, введите адрес электронной почты.");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/auth/createcode", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email }),
      });

      if (response.ok) {
        await AsyncStorage.setItem("email", email);
        router.push("/sign-up");
      } else {
        Alert.alert("Ошибка", "Не удалось отправить код. Попробуйте снова.");
      }
    } catch (error) {
      console.error("Ошибка при отправке email:", error);
      Alert.alert("Ошибка", "Произошла ошибка. Попробуйте снова.");
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Привет! Введи почту для входа</Text>
      <TextInput
        style={styles.input}
        placeholder="Введите адрес электронной почты"
        onChangeText={setEmail}
        value={email}
        keyboardType="email-address"
        autoCapitalize="none"
      />
      <Pressable style={styles.button} onPress={handleSubmit}>
        <Text style={styles.buttonText}>Отправить</Text>
      </Pressable>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 20,
    backgroundColor: "#f5fcff",
  },
  text: {
    marginBottom: 20,
    fontSize: 18,
    textAlign: "center",
  },
  input: {
    height: 40,
    borderColor: "gray",
    borderWidth: 1,
    marginBottom: 20,
    paddingHorizontal: 10,
    borderRadius: 5,
  },
  button: {
    backgroundColor: "#4CAF50",
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 5,
    alignItems: "center",
  },
  buttonText: {
    color: "#fff",
    fontSize: 16,
  },
});

export default AuthLayout;
