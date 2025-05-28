import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { ParkingLotsScreen } from '../screens/ParkingLotsScreen';
import { ParkingLotDetailsScreen } from '../screens/ParkingLotDetailsScreen';
import { colors } from '../utils/theme';

export type RootStackParamList = {
  ParkingLots: undefined;
  ParkingLotDetails: {
    parkingLotId: number;
  };
};

const Stack = createNativeStackNavigator<RootStackParamList>();

export const AppNavigator: React.FC = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="ParkingLots"
        screenOptions={{
          headerStyle: {
            backgroundColor: colors.white,
          },
          headerTintColor: colors.gray[900],
          headerTitleStyle: {
            fontWeight: 'bold',
          },
          headerShadowVisible: false,
        }}
      >
        <Stack.Screen
          name="ParkingLots"
          component={ParkingLotsScreen}
          options={{
            title: 'Parking Lots',
          }}
        />
        <Stack.Screen
          name="ParkingLotDetails"
          component={ParkingLotDetailsScreen}
          options={{
            title: 'Parking Lot Details',
          }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}; 