import React, { useEffect, useState } from 'react';
import {
  StyleSheet,
  View,
  Text,
  ScrollView,
  ActivityIndicator,
  TouchableOpacity,
} from 'react-native';
import { RouteProp, useRoute } from '@react-navigation/native';
import { ParkingLot } from '../types';
import { parkingLots } from '../services/api';
import { colors, spacing, typography } from '../utils/theme';
import { Button } from '../components/Button';

type ParkingLotDetailsRouteParams = {
  ParkingLotDetails: {
    parkingLotId: number;
  };
};

export const ParkingLotDetailsScreen: React.FC = () => {
  const route = useRoute<RouteProp<ParkingLotDetailsRouteParams, 'ParkingLotDetails'>>();
  const { parkingLotId } = route.params;
  const [parkingLot, setParkingLot] = useState<ParkingLot | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchParkingLotDetails();
  }, [parkingLotId]);

  const fetchParkingLotDetails = async () => {
    try {
      const data = await parkingLots.getLot(parkingLotId);
      setParkingLot(data);
    } catch (error) {
      console.error('Error fetching parking lot details:', error);
      // TODO: Show error message to user
    } finally {
      setLoading(false);
    }
  };

  const handleStartParking = () => {
    // TODO: Navigate to start parking session screen
    console.log('Start parking session');
  };

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color={colors.primary} />
      </View>
    );
  }

  if (!parkingLot) {
    return (
      <View style={styles.errorContainer}>
        <Text style={styles.errorText}>Parking lot not found</Text>
      </View>
    );
  }

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.name}>{parkingLot.name}</Text>
        <Text style={styles.description}>{parkingLot.description}</Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Rate</Text>
        <Text style={styles.rate}>${parkingLot.hourly_rate}/hour</Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Capacity</Text>
        <Text style={styles.capacity}>
          {parkingLot.total_spaces} total spaces
        </Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Amenities</Text>
        <View style={styles.amenitiesContainer}>
          {parkingLot.amenities.map((amenity, index) => (
            <View key={index} style={styles.amenityTag}>
              <Text style={styles.amenityText}>{amenity}</Text>
            </View>
          ))}
        </View>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Location</Text>
        <Text style={styles.location}>{parkingLot.location}</Text>
      </View>

      <View style={styles.buttonContainer}>
        <Button
          title="Start Parking Session"
          onPress={handleStartParking}
          variant="primary"
          size="large"
        />
      </View>
    </ScrollView>
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
  errorContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: colors.gray[100],
  },
  errorText: {
    ...typography.body1,
    color: colors.error,
  },
  header: {
    padding: spacing.lg,
    backgroundColor: colors.white,
    borderBottomWidth: 1,
    borderBottomColor: colors.gray[200],
  },
  name: {
    ...typography.h1,
    color: colors.gray[900],
    marginBottom: spacing.xs,
  },
  description: {
    ...typography.body1,
    color: colors.gray[600],
  },
  section: {
    padding: spacing.lg,
    backgroundColor: colors.white,
    marginTop: spacing.md,
  },
  sectionTitle: {
    ...typography.h2,
    color: colors.gray[900],
    marginBottom: spacing.sm,
  },
  rate: {
    ...typography.h3,
    color: colors.primary,
  },
  capacity: {
    ...typography.body1,
    color: colors.gray[700],
  },
  amenitiesContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    marginTop: spacing.xs,
  },
  amenityTag: {
    backgroundColor: colors.gray[200],
    paddingHorizontal: spacing.sm,
    paddingVertical: spacing.xs,
    borderRadius: spacing.xs,
    marginRight: spacing.xs,
    marginBottom: spacing.xs,
  },
  amenityText: {
    ...typography.body2,
    color: colors.gray[700],
  },
  location: {
    ...typography.body1,
    color: colors.gray[700],
  },
  buttonContainer: {
    padding: spacing.lg,
    backgroundColor: colors.white,
    marginTop: spacing.md,
  },
}); 