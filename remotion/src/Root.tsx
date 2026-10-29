import React from 'react';
import {Composition} from 'remotion';
import {Prueba} from './Prueba';

// Proyecto vertical de PHARAON: 1080x1920 a 30 fps.
export const Root: React.FC = () => (
  <Composition id="Prueba" component={Prueba} width={1080} height={1920} fps={30} durationInFrames={60} />
);
