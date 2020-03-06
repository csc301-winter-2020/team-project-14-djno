import React from 'react';
import { shallow } from 'enzyme';
import { SignInWithGoogle } from '../../../src/features/login/SignInWithGoogle';

describe('login/SignInWithGoogle', () => {
  it('renders node with correct class name', () => {
    const props = {
      login: {},
      actions: {},
    };
    const renderedComponent = shallow(
      <SignInWithGoogle {...props} />
    );

    expect(
      renderedComponent.find('.login-sign-in-with-google').length
    ).toBe(1);
  });
});
