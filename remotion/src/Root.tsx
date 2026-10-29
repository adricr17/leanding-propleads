import React from 'react';
import {Composition} from 'remotion';
import {Prueba} from './Prueba';
import {Susto} from './susto/Susto';
import {DURACION, FPS} from './susto/edicion';

// Proyecto vertical de PHARAON: 1080x1920 a 30 fps.
export const Root: React.FC = () => (
  <>
    <Composition id="Prueba" component={Prueba} width={1080} height={1920} fps={30} durationInFrames={60} />
    <Composition id="SustoSiz0" component={Susto} width={1080} height={1920} fps={FPS} durationInFrames={DURACION} />
  </>
);
