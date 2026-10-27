"""
package org.nailyourinterview.lld.parking_lot.strategy.pricing;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.time.Duration;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.temporal.ChronoUnit;

public class TimeBasedPricing implements PricingStrategy {
    // Peak period hours (e.g., 8:00 to 17:00)
    private static final LocalTime PEAK_START = LocalTime.of(8, 0);
    private static final LocalTime PEAK_END = LocalTime.of(17, 0);

    private boolean isPeak(LocalTime time) {
        return !time.isBefore(PEAK_START) && !time.isAfter(PEAK_END);
    }

    @Override
    public double calculateFee(VehicleType type, LocalDateTime entryTime, LocalDateTime exitTime) {
        if (exitTime.isBefore(entryTime)) throw new IllegalArgumentException("Exit time before entry time");

        long durationMinutes = Duration.between(entryTime, exitTime).toMinutes();
        long totalHours = (long) Math.ceil(durationMinutes / 60.0);

        // Count peak hours and non-peak hours by iterating hour by hour
        int peakHours = 0;
        int nonPeakHours = 0;

        LocalDateTime cursor = entryTime.truncatedTo(ChronoUnit.HOURS);
        // If entry time has minutes, consider first hour partially occupied, count as 1 hour anyway (already rounded)
        for (int i = 0; i < totalHours; i++) {
            LocalTime hourStart = cursor.toLocalTime();
            if (isPeak(hourStart)) peakHours++;
            else nonPeakHours++;
            cursor = cursor.plusHours(1);
        }

        double peakRate = switch (type) {
            case CAR -> 30.0;
            case BIKE -> 15.0;
            case TRUCK -> 50.0;
        };

        double nonPeakRate = switch (type) {
            case CAR -> 20.0;
            case BIKE -> 10.0;
            case TRUCK -> 30.0;
        };

        return peakHours * peakRate + nonPeakHours * nonPeakRate;
    }
}
"""
from datetime import datetime, time, timedelta
from math import ceil
from .PricingStrategy import PricingStrategy
from ...enums.VehicleType import VehicleType


class TimeBasedPricing(PricingStrategy):
    PEAK_START = time(8, 0)
    PEAK_END = time(17, 0)

    PEAK_RATES = {
        VehicleType.CAR: 30.0,
        VehicleType.BIKE: 15.0,
        VehicleType.TRUCK: 50.0,
    }

    NON_PEAK_RATES = {
        VehicleType.CAR: 20.0,
        VehicleType.BIKE: 10.0,
        VehicleType.TRUCK: 30.0,
    }

    def calculateFee(self, type: VehicleType, entryTime: datetime, exitTime: datetime) -> float:
        if exitTime < entryTime:
            raise ValueError("Exit time before entry time")

        durationMinutes = (exitTime - entryTime).total_seconds() / 60
        totalHours = int(ceil(durationMinutes / 60.0))

        peakHours = 0
        nonPeakHours = 0
        cursor = entryTime.replace(minute=0, second=0, microsecond=0)

        for i in range(totalHours):
            hourStart = cursor.time()
            if self.PEAK_START <= hourStart <= self.PEAK_END:
                peakHours += 1
            else:
                nonPeakHours += 1
            cursor += timedelta(hours=1)

        peakRate = self.PEAK_RATES.get(type, 0.0)
        nonPeakRate = self.NON_PEAK_RATES.get(type, 0.0)

        return peakHours * peakRate + nonPeakHours * nonPeakRate