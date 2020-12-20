/**
* @jest-environment jsdom
*/

import '../__mocks__/mocks';
import React from 'react'
import { render } from '@testing-library/react-native';
import { act } from 'react-test-renderer';
import configureMockStore from 'redux-mock-store'
import thunk from 'redux-thunk'
import '@react-native-community/async-storage/jest/async-storage-mock';
const middlewares = [thunk]
const mockStore = configureMockStore(middlewares)
import DrawerContent from '../screens/DrawerContent';

test('renders correctly', async () => {
  const test = render(<DrawerContent />).toJSON();
  await act(async () => {expect(test).toMatchSnapshot();})
});