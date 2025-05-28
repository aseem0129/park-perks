import React from 'react';
import { StyleSheet, View, Text, TouchableOpacity } from 'react-native';
import { ParkingLot } from '../types';
import { colors, spacing, shadows } from '../utils/theme';

interface ParkingLotCardProps {
  parkingLot: ParkingLot;
  onPress: (parkingLot: ParkingLot) => void;
}

export const ParkingLotCard: React.FC<ParkingLotCardProps> = ({ parkingLot, onPress }) => {
  const formatPrice = (cents: number) => {
    return `$${(cents / 100).toFixed(2)}/hr`;
  };

  return (
    <TouchableOpacity
      style={styles.container}
      onPress={() => onPress(parkingLot)}
    >
      <View style={styles.content}>
        <Text style={styles.name}>{parkingLot.name}</Text>
        
        {parkingLot.description && (
          <Text style={styles.description} numberOfLines={2}>
            {parkingLot.description}
          </Text>
        )}
        
        <View style={styles.details}>
          <View style={styles.detailItem}>
            <Text style={styles.detailLabel}>Rate</Text>
            <Text style={styles.detailValue}>{formatPrice(parkingLot.hourly_rate)}</Text>
          </View>
          
          <View style={styles.detailItem}>
            <Text style={styles.detailLabel}>Spaces</Text>
            <Text style={styles.detailValue}>{parkingLot.total_spaces}</Text>
          </View>
        </View>
        
        {parkingLot.amenities && parkingLot.amenities.length > 0 && (
          <View style={styles.amenities}>
            {parkingLot.amenities.map((amenity, index) => (
              <View key={index} style={styles.amenityTag}>
                <Text style={styles.amenityText}>{amenity}</Text>
              </View>
            ))}
          </View>
        )}
      </View>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: colors.white,
    borderRadius: 12,
    marginBottom: spacing.md,
    ...shadows.medium,
  },
  content: {
    padding: spacing.md,
  },
  name: {
    fontSize: 18,
    fontWeight: '600',
    color: colors.gray[900],
    marginBottom: spacing.xs,
  },
  description: {
    fontSize: 14,
    color: colors.gray[600],
    marginBottom: spacing.md,
  },
  details: {
    flexDirection: 'row',
    marginBottom: spacing.md,
  },
  detailItem: {
    marginRight: spacing.xl,
  },
  detailLabel: {
    fontSize: 12,
    color: colors.gray[500],
    marginBottom: spacing.xs,
  },
  detailValue: {
    fontSize: 16,
    fontWeight: '600',
    color: colors.gray[900],
  },
  amenities: {
    flexDirection: 'row',
    flexWrap: 'wrap',
  },
  amenityTag: {
    backgroundColor: colors.gray[100],
    paddingHorizontal: spacing.sm,
    paddingVertical: spacing.xs,
    borderRadius: 16,
    marginRight: spacing.xs,
    marginBottom: spacing.xs,
  },
  amenityText: {
    fontSize: 12,
    color: colors.gray[700],
  },
}); 