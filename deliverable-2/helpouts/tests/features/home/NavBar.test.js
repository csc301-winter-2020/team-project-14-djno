import React from 'react';
import { shallow } from 'enzyme';
import { NavBar } from '../../../src/features/home';

it('renders node with correct class name', () => {
  const renderedComponent = shallow(<NavBar />);
  expect(renderedComponent.find('.home-nav-bar').length).toBe(1);
});
