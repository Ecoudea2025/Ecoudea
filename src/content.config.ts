import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const courses = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/courses' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    image: z.string().optional(),
    category: z.string(),
    color: z.string().optional(),
    order: z.number().default(0),
    unlockMode: z.enum(['open', 'sequential']).default('open'),
  }),
});

const classes = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/classes' }),
  schema: z.object({
    title: z.string(),
    course: z.string(),
    order: z.number(),
    classType: z.enum(['clase', 'practica', 'presentacion', 'guia']),
    description: z.string().optional(),
    tags: z.array(z.string()).optional(),
    math: z.boolean().default(false),
    bibliography: z.string().optional(),
    video: z.string().optional(),
    videoPoster: z.string().optional(),
    videoFallback: z.string().optional(),
    videoCaptions: z.string().optional(),
  }),
});

export const collections = { courses, classes };
