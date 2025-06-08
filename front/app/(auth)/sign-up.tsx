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

const SignUp = () => {
  const [code, setCode] = useState("");

  const handleSubmit = async () => {
    const email = await AsyncStorage.getItem("email");
    if (!email) {
      Alert.alert(
        "Ошибка",
        "Не удалось найти email. Пожалуйста, попробуйте снова."
      );
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, code }),
      });

      if (response.ok) {
        Alert.alert("Успех", "Код успешно проверен.");
        const data = await response.json();
        await AsyncStorage.setItem("access_token", data.access_token);
        router.replace("/menu");
      } else {
        Alert.alert("Ошибка", "Неверный код. Попробуйте снова.");
      }
    } catch (error) {
      console.error("Ошибка при проверке кода:", error);
      Alert.alert("Ошибка", "Произошла ошибка. Попробуйте снова.");
    }
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Введите код из письма"
        onChangeText={setCode}
        value={code}
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

export default SignUp;
