import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const OrderCard = ({ orderNumber, storeStreet, deliveryStreet, paymentType, price }) => {
  return (
    <View style={styles.card}>
      <Text style={styles.orderNumber}>Заказ №: {orderNumber}</Text>
      <Text style={styles.info}>Улица магазина: {storeStreet}</Text>
      <Text style={styles.info}>Улица доставки: {deliveryStreet}</Text>
      <Text style={styles.info}>Тип оплаты: {paymentType}</Text>
      <Text style={styles.price}>Цена: {price} руб.</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#fff',
    borderRadius: 8,
    padding: 16,
    marginVertical: 8,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowRadius: 10,
    shadowOffset: { width: 0, height: 2 },
    elevation: 3,
  },
  orderNumber: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  info: {
    fontSize: 16,
    marginBottom: 4,
  },
  price: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#FFA001',
    marginTop: 8,
  },
});

export default OrderCard;