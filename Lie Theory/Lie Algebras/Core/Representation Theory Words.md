The words "$V$ is an $L$-module" and "representation of $L$ on $V$" mean basically the same thing.

In the context of Lie algebra representations, we'll discuss various properties of representations and subrepresentations, followed by the definitions of dual and tensor representations.

### Properties of Representations and Subrepresentations:

1. **Irreducibility**:
   - A representation is **irreducible** if it has no non-trivial proper subrepresentations. In other words, there are no invariant subspaces under the action of the Lie algebra.

1. ==**Complete Reducibility**==:
- Yeah if you reduce completely to irreducible things.

2. **Homomorphism**:
   - A linear map between two representations that preserves the action of the Lie algebra is called a **homomorphism**.

3. **Isomorphism**:
   - Two representations are **isomorphic** if there exists a bijective homomorphism between them.

4. **Equivalence**:
   - Two representations are **equivalent** if they are isomorphic as vector spaces and the action of the Lie algebra is the same.

5. **Trivial Representation**:
   - The trivial representation maps every element of the Lie algebra to the identity element of the vector space.

6. **Adjoint Representation**:
   - The adjoint representation is defined by the action of the Lie algebra on itself through the adjoint map.

### Dual and Tensor Representations:

1. **Dual Representation**:
   - Given a representation of a Lie algebra, the **dual representation** is a new representation on the dual space, where the action of each element of the Lie algebra is taken as the transpose of the action in the original representation. The dual representation is often denoted by putting a star or a superscript 'd' on the original representation.

2. **Tensor Representation**:
   - Given two representations of a Lie algebra, one can form their **tensor product representation**. This new representation acts on the tensor product of the underlying vector spaces of the original representations.

   - The tensor product representation is defined by the action of the Lie algebra on each factor of the tensor product, respecting the bilinearity of the tensor product.

   - If \(V\) and \(W\) are representations of a Lie algebra \(L\), then the tensor product representation is denoted as \(V \otimes W\).

Certainly! In the context of Lie algebras, let's discuss the formulas for the dual and tensor representations.

### Dual Representation:

Given a representation \(V\) of a Lie algebra \(L\), the dual representation \(V^*\) is defined on the dual space \(V^*\) of \(V\) as follows:

1. **Action of Lie Algebra Elements**:

   For \(X \in L\) and \(\phi \in V^*\), the action of \(X\) on \(\phi\) in the dual representation is given by:

   \[ (X \cdot \phi)(v) = -\phi(X \cdot v) \]

   where \(X \cdot v\) denotes the action of \(X\) on \(v\) in the original representation.

2. **Dual Basis**:

   If \(\{e_i\}\) is a basis of \(V\), then the dual basis \(\{\epsilon^i\}\) of \(V^*\) is defined by:

   \[ \epsilon^i(e_j) = \delta^i_j \]

   where \(\delta^i_j\) is the Kronecker delta.

### Tensor Representation:

Given representations \(V\) and \(W\) of a Lie algebra \(L\), the tensor product representation \(V \otimes W\) is defined as follows:

1. **Action of Lie Algebra Elements**:

   For \(X \in L\) and \((v \otimes w) \in V \otimes W\), the action of \(X\) on \(v \otimes w\) is given by:

   \[ X \cdot (v \otimes w) = (X \cdot v) \otimes w + v \otimes (X \cdot w) \]

   where \(X \cdot v\) and \(X \cdot w\) denote the actions of \(X\) on \(v\) and \(w\) in the respective representations.

2. **Basis for Tensor Product**:

   If \(\{e_i\}\) is a basis of \(V\) and \(\{f_j\}\) is a basis of \(W\), then the basis for \(V \otimes W\) is given by the set of all \(e_i \otimes f_j\), where \(e_i\) is from \(V\) and \(f_j\) is from \(W\).

These formulas define how the Lie algebra elements act on the elements of the dual and tensor product representations. They provide a concrete way to compute the action of the Lie algebra on these spaces, making them valuable tools in the study of representations of Lie algebras.