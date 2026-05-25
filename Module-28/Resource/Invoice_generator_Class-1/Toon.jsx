import { encode } from '@toon-format/toon'

function Toon() {
const data = {
  invoiceNumber: 'INV-2025-001',
  date: '2025-12-06',
  customerName: 'John Doe',
  customerEmail: 'john.doe@example.com',
  customerAddress: '123 Main Street, New York, NY 10001',
  items: [
    { id: 1, name: 'Web Development Service', quantity: 40, rate: 75, amount: 3000 },
    { id: 2, name: 'UI/UX Design', quantity: 20, rate: 85, amount: 1700 },
    { id: 3, name: 'Consulting', quantity: 10, rate: 100, amount: 1000 },
    { id: 4, name: 'Project Management', quantity: 15, rate: 90, amount: 1350 }
  ],
  subtotal: 7050,
  tax: 705,
  total: 7755
};
const toonString = encode(data);
console.log(toonString);
  return (
    <div>
      {toonString}
    </div>
  );
}

export default Toon;