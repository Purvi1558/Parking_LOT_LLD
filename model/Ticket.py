"""
package org.nailyourinterview.lld.parking_lot.model;

import lombok.Builder;
import lombok.Data;
import org.nailyourinterview.lld.parking_lot.enums.PaymentStatus;

import java.time.LocalDateTime;

@Data
@Builder
public class Ticket {
    private String ticketId;
    private LocalDateTime entryTime;
    private Vehicle vehicle;
    private String floorId;
    private String spotId;
    private PaymentStatus paymentStatus = PaymentStatus.PENDING;
}
"""
from datetime import datetime
from ..enums.PaymentStatus import PaymentStatus


class Ticket:
    def __init__(self, ticketId: str = None, entryTime: datetime = None, vehicle=None, floorId: str = None, spotId: str = None, paymentStatus=None):
        self.ticketId = ticketId
        self.entryTime = entryTime
        self.vehicle = vehicle
        self.floorId = floorId
        self.spotId = spotId
        self.paymentStatus = paymentStatus if paymentStatus else PaymentStatus.PENDING

    @classmethod
    def builder(cls):
        return TicketBuilder()

    def getTicketId(self) -> str:
        return self.ticketId

    def getEntryTime(self) -> datetime:
        return self.entryTime

    def getVehicle(self):
        return self.vehicle

    def getFloorId(self) -> str:
        return self.floorId

    def getSpotId(self) -> str:
        return self.spotId

    def getPaymentStatus(self):
        return self.paymentStatus

    def setPaymentStatus(self, paymentStatus):
        self.paymentStatus = paymentStatus


class TicketBuilder:
    def __init__(self):
        self._ticketId = None
        self._entryTime = None
        self._vehicle = None
        self._floorId = None
        self._spotId = None

    def ticketId(self, ticketId: str):
        self._ticketId = ticketId
        return self

    def entryTime(self, entryTime: datetime):
        self._entryTime = entryTime
        return self

    def vehicle(self, vehicle):
        self._vehicle = vehicle
        return self

    def floorId(self, floorId: str):
        self._floorId = floorId
        return self

    def spotId(self, spotId: str):
        self._spotId = spotId
        return self

    def build(self) -> Ticket:
        return Ticket(
            ticketId=self._ticketId,
            entryTime=self._entryTime,
            vehicle=self._vehicle,
            floorId=self._floorId,
            spotId=self._spotId,
        )
