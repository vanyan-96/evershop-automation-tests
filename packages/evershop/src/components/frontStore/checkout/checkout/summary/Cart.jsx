import PropTypes from 'prop-types';
import React from 'react';
import { Discount } from '@components/frontStore/checkout/checkout/summary/cart/Discount';
import { Shipping } from '@components/frontStore/checkout/checkout/summary//cart/Shipping';
import { Subtotal } from '@components/frontStore/checkout/checkout/summary//cart/Subtotal';
import { Tax } from '@components/frontStore/checkout/checkout/summary//cart/Tax';
import { Total } from '@components/frontStore/checkout/checkout/summary//cart/Total';

function CartSummary({
  totalQty,
  subTotal,
  subTotalInclTax,
  grandTotal,
  discountAmount,
  taxAmount,
  shippingMethodName,
  shippingFeeInclTax,
  coupon,
  priceIncludingTax
}) {
  return (
    <div className="checkout-summary-block">
      <Subtotal
        count={totalQty}
        total={priceIncludingTax ? subTotalInclTax.text : subTotal.text}
      />
      <Shipping method={shippingMethodName} cost={shippingFeeInclTax.text} />
      {!priceIncludingTax && <Tax amount={taxAmount.text} />}
      <Discount code={coupon} discount={discountAmount.text} />
      <Total
        taxAmount={taxAmount.text}
        total={grandTotal.text}
        priceIncludingTax={priceIncludingTax}
      />
    </div>
  );
}

CartSummary.propTypes = {
  coupon: PropTypes.string,
  discountAmount: PropTypes.shape({
    text: PropTypes.string.isRequired
  }),
  grandTotal: PropTypes.shape({
    text: PropTypes.string.isRequired
  }),
  shippingFeeInclTax: PropTypes.shape({
    text: PropTypes.string.isRequired
  }),
  shippingMethodName: PropTypes.string,
  subTotal: PropTypes.shape({
    text: PropTypes.string.isRequired
  }),
  subTotalInclTax: PropTypes.shape({
    text: PropTypes.string.isRequired
  }),
  taxAmount: PropTypes.shape({
    text: PropTypes.string.isRequired
  }),
  totalQty: PropTypes.string,
  priceIncludingTax: PropTypes.bool
};

CartSummary.defaultProps = {
  coupon: '',
  discountAmount: {
    text: ''
  },
  grandTotal: {
    text: ''
  },
  shippingFeeInclTax: {
    text: ''
  },
  shippingMethodName: '',
  subTotal: {
    text: ''
  },
  subTotalInclTax: {
    text: ''
  },
  taxAmount: {
    text: ''
  },
  totalQty: '',
  priceIncludingTax: false
};

export { CartSummary };
