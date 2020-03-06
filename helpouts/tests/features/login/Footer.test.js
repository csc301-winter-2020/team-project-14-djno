import React from 'react';
import { shallow } from 'enzyme';
import { Footer } from '../../../src/features/login/Footer';

describe('login/Footer', () => {
  it('renders node with correct class name', () => {
    const props = {
      login: {},
      actions: {},
    };
    const renderedComponent = shallow(
      <Footer {...props} />
    );

    expect(
      renderedComponent.find('.login-footer').length
    ).toBe(1);
  });
});
