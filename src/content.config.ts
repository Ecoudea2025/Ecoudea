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
    /** Crédito visible del material heredado (autor, institución) */
    author: z.string().optional(),
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
    /** Conceptos clave: alimentan el glosario y la búsqueda */
    conceptos: z.array(z.string()).optional(),
    /** Unidad temática (agrupa el listado del curso; sin unidades, un solo grupo) */
    unit: z.string().optional(),
    /** Borrador: no se publica (ni página, ni listados, ni sitemap, ni búsqueda) */
    draft: z.boolean().default(false),
  }),
});

export const collections = { courses, classes };
