export interface User {
  id: number;
  email: string;
  full_name: string;
  user_type: 'student' | 'business' | 'admin';
  university?: string;
  student_id?: string;
  major?: string;
  graduation_year?: number;
  interests?: string[];
  is_active: boolean;
  is_verified: boolean;
}

export interface ParkingSession {
  id: number;
  user_id: number;
  parking_lot_id: number;
  business_sponsor_id?: number;
  start_time: string;
  end_time: string;
  status: 'pending' | 'active' | 'completed' | 'cancelled';
  original_cost: number;
  sponsored_amount?: number;
  final_cost: number;
  business_visit_time?: string;
  business_visit_status?: string;
  visit_feedback?: Record<string, any>;
}

export interface ParkingLot {
  id: number;
  name: string;
  location: {
    latitude: number;
    longitude: number;
  };
  total_spaces: number;
  hourly_rate: number;
  university_id?: number;
  description?: string;
  amenities?: string[];
  operating_hours?: Record<string, string>;
}

export interface BusinessSponsorship {
  id: number;
  business_id: number;
  campaign_name: string;
  start_date: string;
  end_date: string;
  daily_budget: number;
  max_sponsored_hours: number;
  target_audience: Record<string, any>;
  promotion_details: Record<string, any>;
  total_spent: number;
  total_impressions: number;
  total_visits: number;
} 