import React, { useEffect, useState } from 'react';
import {
  StyleSheet,
  View,
  FlatList,
  ActivityIndicator,
  RefreshControl,
} from 'react-native';
import { useNavigation } from '@react-navigation/native';
import { NativeStackNavigationProp } from '@react-navigation/native-stack';
import { ParkingLot } from '../types';
import { ParkingLotCard } from '../components/ParkingLotCard';
import { parkingLots } from '../services/api';
import { colors, spacing } from '../utils/theme';
import { RootStackParamList } from '../navigation/AppNavigator';

type ParkingLotsScreenNavigationProp = NativeStackNavigationProp<
  RootStackParamList,
  'ParkingLots'
>;

export const ParkingLotsScreen: React.FC = () => {
  const navigation = useNavigation<ParkingLotsScreenNavigationProp>();
  const [lots, setLots] = useState<ParkingLot[]>([]);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);

  const fetchParkingLots = async () => {
    try {
      const data = await parkingLots.getLots();
      setLots(data);
    } catch (error) {
      console.error('Error fetching parking lots:', error);
      // TODO: Show error message to user
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  useEffect(() => {
    fetchParkingLots();
  }, []);

  const handleRefresh = () => {
    setRefreshing(true);
    fetchParkingLots();
  };

  const handleParkingLotPress = (parkingLot: ParkingLot) => {
    navigation.navigate('ParkingLotDetails', {
      parkingLotId: parkingLot.id,
    });
  };

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color={colors.primary} />
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <FlatList
        data={lots}
        renderItem={({ item }) => (
          <ParkingLotCard
            parkingLot={item}
            onPress={handleParkingLotPress}
          />
        )}
        keyExtractor={(item) => item.id.toString()}
        contentContainerStyle={styles.listContent}
        refreshControl={
          <RefreshControl
            refreshing={refreshing}
            onRefresh={handleRefresh}
            colors={[colors.primary]}
          />
        }
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.gray[100],
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: colors.gray[100],
  },
  listContent: {
    padding: spacing.md,
  },
}); 