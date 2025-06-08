import OrderCard from "@/components/OrderCard";
import React from "react";
import { ScrollView, StyleSheet } from "react-native";

const orders = [
  {
    orderNumber: "12345",
    storeStreet: "ул. Пушкина, 10",
    deliveryStreet: "ул. Ленина, 20",
    paymentType: "Карта",
    price: "1500",
  },
  {
    orderNumber: "67890",
    storeStreet: "ул. Гагарина, 15",
    deliveryStreet: "ул. Космонавтов, 25",
    paymentType: "Наличные",
    price: "2500",
  },
];

const Orders = () => {
  return (
    <ScrollView style={styles.container}>
      {orders.map((order, index) => (
        <OrderCard
          key={index}
          orderNumber={order.orderNumber}
          storeStreet={order.storeStreet}
          deliveryStreet={order.deliveryStreet}
          paymentType={order.paymentType}
          price={order.price}
        />
      ))}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: "#f5fcff",
  },
});

export default Orders;
