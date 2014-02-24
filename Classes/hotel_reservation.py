class HotelRoom:
	def __init__(self, category, total):
		self.bookcount = 0
		self.category = category
		self.total = total

	def book(self, bookcount):
		self.bookcount += bookcount

	def cancel(self, cancelcount):
		self.bookcount -= cancelcount


class Reservation:
	def __init__(self, penthhouse, singleroom):
		self.penthhouse = penthhouse
		self.singleroom = singleroom

	def reservation(self, category, mode, count):
		if self.penthhouse.category == category:
			if mode == 'book':
				self.penthhouse.book(count)
			elif mode == 'cancel':
				self.penthhouse.cancel(count)
		elif category == self.singleroom.category:
			if mode == 'book':
				self.singleroom.book(count)
			elif mode == 'cancel':
				self.singleroom.cancel(count)

	def print_reservation(self):
		print 'penthhouse booked: %d total: %d' % (self.penthhouse.bookcount, self.penthhouse.total)
		print 'singleroom booked: %d total: %d' % (self.singleroom.bookcount, self.singleroom.total)
		print '\n'

if __name__ == '__main__':
	hr1 = HotelRoom('penthhouse', 10)
	hr2 = HotelRoom('singleroom', 20)

	rsv = Reservation(hr1, hr2)

	rsv.reservation('penthhouse', 'book', 2)
	rsv.print_reservation()

	rsv.reservation('singleroom', 'book', 4)
	rsv.print_reservation()

	rsv.reservation('penthhouse', 'cancel', 1)
	rsv.reservation('singleroom', 'cancel', 3)
	rsv.print_reservation()
