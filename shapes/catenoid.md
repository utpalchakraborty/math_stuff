# The Catenoid: A Remarkable Minimal Surface

![catenoid](../images/catenoid.png)

## Definition and Parametrization

The catenoid is a surface of revolution obtained by rotating a catenary curve around an axis. It was discovered by Euler in 1744 and is historically significant as the first minimal surface to be discovered other than the plane.

### Parametric Equations

For a catenoid with scale parameter $$a$$, the surface is described by:

$$
\begin{align*}
x &= a\cosh(v)\cos(u) \\
y &= a\cosh(v)\sin(u) \\
z &= av
\end{align*}
$$

where the parameters are:

- u: rotation parameter, with $u \in [0, 2\pi]$
- v: height parameter
- a: scale parameter determining the throat size

## Key Properties

### 1. Minimal Surface

The catenoid is a minimal surface, meaning its mean curvature $$H$$ is zero everywhere:

$$H = \frac{\kappa_1 + \kappa_2}{2} = 0$$

where $$\kappa_1$$ and $$\kappa_2$$ are the principal curvatures at any point.

### 2. First Fundamental Form

The coefficients of the first fundamental form are:

$$
\begin{align*}
E &= a^2\cosh^2(v) \\
F &= 0 \\
G &= a^2(\cosh^2(v) + 1)
\end{align*}
$$

### 3. Surface Area

For a catenoid bounded by two parallel circles of radius $$r$$ at height $$±h$$, the surface area is:

$$A = 2\pi a^2 \int_{-h/a}^{h/a} \cosh(v)\sqrt{1 + \cosh^2(v)} \, dv$$

### 4. Physical Realization

The catenoid naturally appears as the shape assumed by a soap film suspended between two parallel circular rings. This is because soap films minimize their surface area due to surface tension, forming minimal surfaces.

## Special Properties

1. **Uniqueness**: The catenoid is the only minimal surface of revolution besides the plane.

2. **Isometry**: The catenoid is locally isometric to the helicoid, meaning there exists a length-preserving map between small neighborhoods on these surfaces.

3. **Gaussian Curvature**: At any point (u,v), the Gaussian curvature K is given by:

   $$K = -\frac{1}{a^2\cosh^4(v)}$$

4. **Cross Sections**:
   - Horizontal sections (constant z) are circles
   - Vertical sections through the axis are catenaries
   - The "waist" or throat occurs at v = 0, with radius a

## Physical Applications

1. **Soap Films**: The catenoid shape appears in soap films between circular rings
2. **Architecture**: Used in minimal surface architecture for both aesthetic and structural efficiency
3. **Liquid Bridges**: Describes the shape of liquid bridges between circular supports

## Stability Properties

The catenoid exhibits interesting stability properties. For two parallel rings of radius R separated by distance h:

1. When h/R < 1.325..., there exist two catenoids
2. When h/R = 1.325..., there exists exactly one catenoid
3. When h/R > 1.325..., no stable catenoid exists

This explains why soap films between rings collapse when pulled too far apart.

## Relation to Other Surfaces

The catenoid is part of a family of associated minimal surfaces that includes:

1. The helicoid (through the Bonnet transformation)
2. Enneper's surface (through complex parameter substitution)
3. Costa's surface (as a limiting case)

These relationships reveal deep connections in differential geometry between seemingly different minimal surfaces.
