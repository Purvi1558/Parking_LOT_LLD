"""
package org.nailyourinterview.lld.parking_lot.strategy.pricing;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.time.Duration;
import java.time.LocalDateTime;
import java.util.Map;

public class EventBasedPricing implements PricingStrategy {
    // Event pricing: Higher per-hour rates
    private static final Map<VehicleType, Double> EVENT_HOURLY_RATES = Map.of(
            VehicleType.CAR, 50.0,
            VehicleType.BIKE, 30.0,
            VehicleType.TRUCK, 70.0
    );

    @Override
    public double calculateFee(VehicleType type, LocalDateTime entryTime, LocalDateTime exitTime) {
        long durationMinutes = Duration.between(entryTime, exitTime).toMinutes();
        long hours = (long) Math.ceil(durationMinutes / 60.0); // always round up to next hour

        double ratePerHour = EVENT_HOURLY_RATES.getOrDefault(type, 0.0);
        return ratePerHour * hours;
    }
}
"""
from typing import Optional
from .PricingStrategy import PricingStrategy
from ...enums.VehicleType import VehicleType
from datetime import datetime
from math import ceil

class EventBasedPricing(PricingStrategy):
    EVENT_HOURLY_RATES = {
            VehicleType.CAR: 50.0,
            VehicleType.BIKE: 30.0,
            VehicleType.TRUCK: 70.0
    }
    def calculateFee(self, type: VehicleType, entryTime: datetime, exitTime: datetime) -> float:
        durationMinutes = (exitTime - entryTime).total_seconds() / 60
        hours = ceil(durationMinutes / 60.0)
        ratePerHour = self.EVENT_HOURLY_RATES.get(type, 0.0)
        return ratePerHour * hours
            