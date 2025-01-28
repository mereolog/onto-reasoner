(cl:comment '
BFO 2020 Axiomatization, generated 2024/01/08
The most current version of this file will always be at the GitHub repository https://github.com/bfo-ontology/bfo-2020
Author: Alan Ruttenberg - alanruttenberg(at)gmail.com
This work is licensed under a Creative Commons "Attribution 4.0 International" license: https://creativecommons.org/licenses/by/4.0/'

 (cl:text

  (cl:ttl https://basic-formal-ontology.org/2020/formulas/clif/occurrent-mereology.cl

   (cl:outdiscourse continuant-part-of spatially-projects-onto temporally-projects-onto has-last-instant has-first-instant occupies-temporal-region temporal-part-of proper-temporal-part-of exists-at instance-of has-proper-occurrent-part proper-occurrent-part-of has-occurrent-part occurrent-part-of)

  (cl:comment "occurrent-part-of and has-occurrent-part are inverse relations [yvi-1]"
    (forall (a b) (iff (occurrent-part-of a b) (has-occurrent-part b a))))


  (cl:comment "proper-occurrent-part-of and has-proper-occurrent-part are inverse relations [wim-1]"
    (forall (a b)
     (iff (proper-occurrent-part-of a b) (has-proper-occurrent-part b a))))


  (cl:comment "occurrent-part-of is reflexive [hbj-1]"
    (forall (a)
     (if (exists (t) (instance-of a occurrent t))
      (occurrent-part-of a a))))


  (cl:comment "occurrent-part-of is antisymmetric [xlu-1]"
    (forall (a b)
     (if (and (occurrent-part-of a b) (occurrent-part-of b a)) (= a b))))


  (cl:comment "A proper occurrent part of b means a is an occurrent part of b and a is not the same as b [okr-1]"
    (forall (x y)
     (iff (proper-occurrent-part-of x y)
      (and (occurrent-part-of x y) (not (= x y))))))


  (cl:comment "occurrent-part-of is transitive [kad-1]"
    (forall (a b c)
     (if (and (occurrent-part-of a b) (occurrent-part-of b c))
      (occurrent-part-of a c))))


  (cl:comment "If one occurrent is part of another, then the temporal region on which the former projects is a part of the temporal region on which the latter projects [ybr-1]"
    (forall (o1 o2)
     (if (occurrent-part-of o1 o2)
      (forall (t) (if (exists-at o1 t) (exists-at o2 t))))))


  (cl:comment "If a occurrent-part-of b then if a is an instance of temporal-region then b is an instance of temporal-region, and vice-versa [gjl-2]"
    (forall (p q)
     (if (occurrent-part-of p q)
      (iff (instance-of p temporal-region p)
       (instance-of q temporal-region q)))))


  (cl:comment "occurrent-part-of has domain occurrent and range occurrent [zmr-1]"
    (forall (a b)
     (if (occurrent-part-of a b)
      (and (exists (t) (instance-of a occurrent t))
       (exists (t) (instance-of b occurrent t))))))


  (cl:comment "If a occurrent-part-of b then if a is an instance of process then b is an instance of process [csk-1]"
    (forall (p q)
     (if (occurrent-part-of p q)
      (if (exists (t) (instance-of p process t))
       (exists (t) (instance-of q process t))))))


  (cl:comment "proper-temporal-part-of has domain occurrent and range occurrent [ees-1]"
    (forall (a b)
     (if (proper-temporal-part-of a b)
      (and (exists (t) (instance-of a occurrent t))
       (exists (t) (instance-of b occurrent t))))))


  (cl:comment "proper-occurrent-part-of has domain occurrent and range occurrent [yhc-1]"
    (forall (a b)
     (if (proper-occurrent-part-of a b)
      (and (exists (t) (instance-of a occurrent t))
       (exists (t) (instance-of b occurrent t))))))


  (cl:comment "every process has a process boundary [aff-1]"
    (forall (p)
     (if (exists (t) (instance-of p process t))
      (exists (pb t)
       (and (instance-of pb process-boundary t)
        (occurrent-part-of pb p))))))


  (cl:comment "definition of temporal part for temporal regions [cmy-2]"
    (forall (b c)
     (if
      (and (instance-of b temporal-region b)
       (instance-of c temporal-region c))
      (iff (temporal-part-of b c) (occurrent-part-of b c)))))


  (cl:comment "If a has-occurrent-part b then if a is an instance of process-boundary then b is an instance of process-boundary [hdk-1]"
    (forall (p q)
     (if (has-occurrent-part p q)
      (if (exists (t) (instance-of p process-boundary t))
       (exists (t) (instance-of q process-boundary t))))))


  (cl:comment "If a occurrent-part-of b then if a is an instance of spatiotemporal-region then b is an instance of spatiotemporal-region, and vice-versa [myl-1]"
    (forall (p q)
     (if (occurrent-part-of p q)
      (iff (exists (t) (instance-of p spatiotemporal-region t))
       (exists (t) (instance-of q spatiotemporal-region t))))))


  (cl:comment "If a has-occurrent-part b then if a is an instance of process then b is an instance of process or process-boundary  [ccz-1]"
    (forall (p q)
     (if (has-occurrent-part p q)
      (if (exists (t) (instance-of p process t))
       (exists (t)
        (or (instance-of q process t)
         (instance-of q process-boundary t)))))))


  (cl:comment "If a occurrent-part-of b then if a is an instance of process-boundary then b is an instance of process or process-boundary  [ptm-1]"
    (forall (p q)
     (if (occurrent-part-of p q)
      (if (exists (t) (instance-of p process-boundary t))
       (exists (t)
        (or (instance-of q process t)
         (instance-of q process-boundary t)))))))


  (cl:comment "a process boundary is any temporal part of a process that has no proper temporal parts. [esh-1]"
    (forall (pb)
     (iff (exists (t) (instance-of pb process-boundary t))
      (and
       (exists (p)
        (and (temporal-part-of pb p)
         (exists (t) (instance-of p process t))))
       (exists (t)
        (and (occupies-temporal-region pb t)
         (instance-of t temporal-instant t)))))))


  (cl:comment "occurrent-part-of has a unique product [hpc-1]"
    (forall (x y)
     (if
      (exists (t)
       (and (instance-of x occurrent t) (instance-of y occurrent t)
        (instance-of t temporal-region t)))
      (if
       (exists (w) (and (occurrent-part-of w x) (occurrent-part-of w y)))
       (exists (z)
        (forall (w)
         (iff (occurrent-part-of w z)
          (and (occurrent-part-of w x) (occurrent-part-of w y)))))))))


  (cl:comment "At least one process boundary needs to be at the first or last instant of the process it bounds [qsp-1]"
    (forall (p)
     (if (exists (tp) (instance-of p process tp))
      (exists (pb tb tp)
       (and (occupies-temporal-region p tp) (occurrent-part-of pb p)
        (occupies-temporal-region pb tb)
        (instance-of pb process-boundary tb)
        (exists (ltp ftp)
         (and (has-first-instant tp ftp) (has-last-instant tp ltp)
          (or (= tb ftp) (= tb ltp)))))))))


  (cl:comment "b temporal part c (both spatiotemporal regions) iff b temporal projection is part of c's temporal projection, and for all parts of b's existence, if it spatially-projects-onto s at that time, then so does c [eom-2]"
    (forall (b c)
     (if
      (and (exists (t) (instance-of b spatiotemporal-region t))
       (exists (t) (instance-of c spatiotemporal-region t)))
      (iff (temporal-part-of b c)
       (exists (tb tc)
        (and (temporally-projects-onto b tb)
         (temporally-projects-onto c tc) (occurrent-part-of tb tc)
         (forall (tp)
          (if
           (and (occurrent-part-of tp tb)
            (exists (s) (spatially-projects-onto b s tp)))
           (exists (s)
            (and (spatially-projects-onto b s tp)
             (spatially-projects-onto c s tp)))))))))))


  (cl:comment "Two spatiotemporal regions are parts when they are temporal parts and their spatial projects are always parts [txf-1]"
    (forall (st1 st2)
     (if
      (and (exists (t) (instance-of st1 spatiotemporal-region t))
       (exists (t) (instance-of st2 spatiotemporal-region t)))
      (iff (occurrent-part-of st1 st2)
       (and
        (exists (t1 t2)
         (and (temporally-projects-onto st1 t1)
          (temporally-projects-onto st2 t2) (temporal-part-of t1 t2)))
        (forall (t)
         (if (exists-at st1 t)
          (exists (s1 s2 tp)
           (and (temporal-part-of tp t)
            (spatially-projects-onto st1 s1 tp)
            (spatially-projects-onto st2 s2 tp)
            (continuant-part-of s1 s2 tp))))))))))

)))(cl:comment '
BFO 2020 Axiomatization, generated 2024/01/08
The most current version of this file will always be at the GitHub repository https://github.com/bfo-ontology/bfo-2020
Author: Alan Ruttenberg - alanruttenberg(at)gmail.com
This work is licensed under a Creative Commons "Attribution 4.0 International" license: https://creativecommons.org/licenses/by/4.0/'

 (cl:text

  (cl:ttl https://basic-formal-ontology.org/2020/formulas/clif/history.cl

   (cl:outdiscourse participates-in exists-at instance-of has-history history-of)

  (cl:comment "history-of and has-history are inverse relations [abx-1]"
    (forall (a b) (iff (history-of a b) (has-history b a))))


  (cl:comment "history-of is functional on second argument [zek-1]"
    (forall (p q r) (if (and (history-of p q) (history-of p r)) (= q r))))


  (cl:comment "history-of is functional on first argument [woe-1]"
    (forall (p q r) (if (and (history-of p q) (history-of r q)) (= p r))))


  (cl:comment "every history is the history of something [vvy-1]"
    (forall (h)
     (if (exists (t) (instance-of h history t))
      (exists (m) (history-of h m)))))


  (cl:comment "every material-entity has a history [okt-1]"
    (forall (m)
     (if (exists (t) (instance-of m material-entity t))
      (exists (h) (history-of h m)))))


  (cl:comment "a material entity participates in its history [lga-1]"
    (forall (h m)
     (if (history-of h m)
      (forall (t) (if (exists-at m t) (participates-in m h t))))))


  (cl:comment "material entity and its history exist at exactly the same times [uzz-1]"
    (forall (m h)
     (if (history-of h m)
      (forall (t)
       (iff (instance-of m material-entity t)
        (instance-of h history t))))))


  (cl:comment "history-of has domain history and range material-entity [rph-1]"
    (forall (a b)
     (if (history-of a b)
      (and (exists (t) (instance-of a history t))
       (exists (t) (instance-of b material-entity t))))))

)))(cl:comment '
BFO 2020 Axiomatization, generated 2024/01/08
The most current version of this file will always be at the GitHub repository https://github.com/bfo-ontology/bfo-2020
Author: Alan Ruttenberg - alanruttenberg(at)gmail.com
This work is licensed under a Creative Commons "Attribution 4.0 International" license: https://creativecommons.org/licenses/by/4.0/'

 (cl:text

  (cl:ttl https://basic-formal-ontology.org/2020/formulas/clif/participation.cl

   (cl:outdiscourse exists-at occurrent-part-of concretizes specifically-depends-on occupies-temporal-region temporal-part-of instance-of has-participant participates-in)

  (cl:comment "participates-in and has-participant are inverse relations [xjr-1]"
    (forall (t a b) (iff (participates-in a b t) (has-participant b a t))))


  (cl:comment "At every time a process exists it has a participant [trl-1]"
    (forall (p t)
     (if (instance-of p process t) (exists (c) (participates-in c p t)))))


  (cl:comment "participates-in is dissective on third argument, a temporal region [yjm-1]"
    (forall (p q r s)
     (if (and (participates-in p q r) (temporal-part-of s r))
      (participates-in p q s))))


  (cl:comment "If c participates in p at t and p occupies-temporal-region r then t is part of r [kxe-1]"
    (forall (c p r t)
     (if (and (occupies-temporal-region p r) (participates-in c p t))
      (temporal-part-of t r))))


  (cl:comment "participates-in is time indexed and has domain: independent-continuant but not spatial-region or specifically-dependent-continuant or generically-dependent-continuant  and range: process [ild-1]"
    (forall (a b t)
     (if (participates-in a b t)
      (and
       (or
        (and (instance-of a independent-continuant t)
         (not (instance-of a spatial-region t)))
        (instance-of a specifically-dependent-continuant t)
        (instance-of a generically-dependent-continuant t))
       (instance-of b process t) (instance-of t temporal-region t)))))


  (cl:comment "At every time a specific dependent s participates in a process p there's a part of that time, during which there's an independent-continuant that s s-depends on, and that participates in p at that time [cgn-1]"
    (forall (sdc p t)
     (if
      (and (instance-of sdc specifically-dependent-continuant t)
       (participates-in sdc p t))
      (exists (tp ic)
       (and (instance-of tp temporal-region tp) (temporal-part-of tp t)
        (instance-of ic independent-continuant tp)
        (not (instance-of ic spatial-region tp))
        (specifically-depends-on sdc ic) (participates-in ic p tp))))))


  (cl:comment "If a generically dependent continuant participates in a process p then, if it is concretized as a process, that process is part of p, fand if concretized as an sdc then the bearer of that sdc participates in the process [fmm-1]"
    (forall (gdc p t)
     (if
      (and (instance-of gdc generically-dependent-continuant t)
       (participates-in gdc p t))
      (exists (tp b)
       (and (temporal-part-of tp t) (concretizes b gdc tp)
        (or
         (and (instance-of b specifically-dependent-continuant tp)
          (exists (ic)
           (and (specifically-depends-on b ic)
            (participates-in ic p tp))))
         (and (occurrent-part-of b p) (exists-at b tp))))))))

)))(cl:comment '
BFO 2020 Axiomatization, generated 2024/01/08
The most current version of this file will always be at the GitHub repository https://github.com/bfo-ontology/bfo-2020
Author: Alan Ruttenberg - alanruttenberg(at)gmail.com
This work is licensed under a Creative Commons "Attribution 4.0 International" license: https://creativecommons.org/licenses/by/4.0/'

 (cl:text

  (cl:ttl https://basic-formal-ontology.org/2020/formulas/clif/generic-dependence.cl

   (cl:outdiscourse exists-at occurrent-part-of specifically-depends-on participates-in inheres-in instance-of temporal-part-of is-carrier-of generically-depends-on is-concretized-by concretizes)

  (cl:comment "concretizes and is-concretized-by are inverse relations [zba-1]"
    (forall (t a b) (iff (concretizes a b t) (is-concretized-by b a t))))


  (cl:comment "generically-depends-on and is-carrier-of are inverse relations [mvp-1]"
    (forall (t a b)
     (iff (generically-depends-on a b t) (is-carrier-of b a t))))


  (cl:comment "concretizes is dissective on third argument, a temporal region [nyz-1]"
    (forall (p q r s)
     (if (and (concretizes p q r) (temporal-part-of s r))
      (concretizes p q s))))


  (cl:comment "A generically dependent continuant is at all times at which it exists concretized by something [ibk-1]"
    (forall (t g)
     (if (instance-of g generically-dependent-continuant t)
      (exists (s tp) (and (temporal-part-of tp t) (concretizes s g tp))))))


  (cl:comment "a g-dependent continuant b g-depends on an independent continuant c at t means: there inheres in c at t an s-dependent continuant which concretizes b at t [otx-1]"
    (forall (g c t)
     (if (generically-depends-on g c t)
      (exists (s tp)
       (and (temporal-part-of tp t) (inheres-in s c)
        (concretizes s g tp))))))


  (cl:comment "concretizes is time indexed and has domain: specifically-dependent-continuant or process  and range: generically-dependent-continuant [rog-1]"
    (forall (a b t)
     (if (concretizes a b t)
      (and
       (or (instance-of a specifically-dependent-continuant t)
        (instance-of a process t))
       (instance-of b generically-dependent-continuant t)
       (instance-of t temporal-region t)))))


  (cl:comment "generically-depends-on is time indexed and has domain: generically-dependent-continuant and range: independent-continuant but not spatial-region [ekp-1]"
    (forall (a b t)
     (if (generically-depends-on a b t)
      (and (instance-of a generically-dependent-continuant t)
       (and (instance-of b independent-continuant t)
        (not (instance-of b spatial-region t)))
       (instance-of t temporal-region t)))))


  (cl:comment "If a specifically-dependent-continuant concretizes a gdc then the gdc generically-depends-on the bearer of the sdc [cik-1]"
    (forall (g b sdc)
     (if
      (and
       (exists (t) (instance-of g generically-dependent-continuant t))
       (exists (t) (instance-of sdc specifically-dependent-continuant t))
       (exists (t) (instance-of b independent-continuant t)))
      (forall (t)
       (if (and (concretizes sdc g t) (inheres-in sdc b))
        (generically-depends-on g b t))))))


  (cl:comment "If a generically dependent continuant participates in a process p then, if it is concretized as a process, that process is part of p, fand if concretized as an sdc then the bearer of that sdc participates in the process [fmm-1]"
    (forall (gdc p t)
     (if
      (and (instance-of gdc generically-dependent-continuant t)
       (participates-in gdc p t))
      (exists (tp b)
       (and (temporal-part-of tp t) (concretizes b gdc tp)
        (or
         (and (instance-of b specifically-dependent-continuant tp)
          (exists (ic)
           (and (specifically-depends-on b ic)
            (participates-in ic p tp))))
         (and (occurrent-part-of b p) (exists-at b tp))))))))

)))(cl:comment '
BFO 2020 Axiomatization, generated 2024/01/08
The most current version of this file will always be at the GitHub repository https://github.com/bfo-ontology/bfo-2020
Author: Alan Ruttenberg - alanruttenberg(at)gmail.com
This work is licensed under a Creative Commons "Attribution 4.0 International" license: https://creativecommons.org/licenses/by/4.0/'

 (cl:text

  (cl:ttl https://basic-formal-ontology.org/2020/formulas/clif/continuant-mereology.cl

   (cl:outdiscourse occupies-spatial-region temporal-part-of exists-at has-proper-continuant-part proper-continuant-part-of instance-of has-continuant-part continuant-part-of)

  (cl:comment "continuant-part-of and has-continuant-part are inverse relations [eld-1]"
    (forall (t a b)
     (iff (continuant-part-of a b t) (has-continuant-part b a t))))


  (cl:comment "continuant-part-of is reflexive at a time [mcd-1]"
    (forall (a t)
     (if (instance-of a independent-continuant t)
      (continuant-part-of a a t))))


  (cl:comment "proper-continuant-part-of and has-proper-continuant-part are inverse relations [hpm-1]"
    (forall (t a b)
     (iff (proper-continuant-part-of a b t)
      (has-proper-continuant-part b a t))))


  (cl:comment "exists-at is dissective on first argumentwhen it is a continuant [uns-1]"
    (forall (p q r)
     (if (and (exists-at p q) (continuant-part-of r p q))
      (exists-at r q))))


  (cl:comment "A fiat point has no parts other than itself [jgo-1]"
    (forall (fp t p)
     (if (and (instance-of fp fiat-point t) (continuant-part-of p fp t))
      (= p fp))))


  (cl:comment "continuant-part-of is dissective on third argument, a temporal region [mqp-1]"
    (forall (p q r s)
     (if (and (continuant-part-of p q r) (temporal-part-of s r))
      (continuant-part-of p q s))))


  (cl:comment "If a has-continuant-part b then if a is an instance of fiat-point then b is an instance of fiat-point [jqd-1]"
    (forall (p q t)
     (if (and (has-continuant-part p q t) (instance-of p fiat-point t))
      (instance-of q fiat-point t))))


  (cl:comment "x proper continuant part of y means x is a continuant part of y but y is not continuant part of x [sls-1]"
    (forall (x y t)
     (iff (proper-continuant-part-of x y t)
      (and (continuant-part-of x y t) (not (continuant-part-of y x t))))))


  (cl:comment "proper-continuant-part-of is dissective on third argument, a temporal region [vjv-1]"
    (forall (p q r s)
     (if (and (proper-continuant-part-of p q r) (temporal-part-of s r))
      (proper-continuant-part-of p q s))))


  (cl:comment "If a continuant-part-of b then if a is an instance of material-entity then b is an instance of material-entity [dok-1]"
    (forall (p q t)
     (if
      (and (continuant-part-of p q t) (instance-of p material-entity t))
      (instance-of q material-entity t))))


  (cl:comment "If a continuant-part-of b then if a is an instance of spatial-region then b is an instance of spatial-region, and vice-versa [kbr-1]"
    (forall (p q t)
     (if (continuant-part-of p q t)
      (iff (instance-of p spatial-region t)
       (and (instance-of q spatial-region t))))))


  (cl:comment "If a has-continuant-part b then if a is an instance of fiat-surface then b is an instance of continuant-fiat-boundary [ysp-1]"
    (forall (p q t)
     (if (and (has-continuant-part p q t) (instance-of p fiat-surface t))
      (instance-of q continuant-fiat-boundary t))))


  (cl:comment "If a has-continuant-part b then if a is an instance of three-dimensional-spatial-region then b is an instance of spatial-region [fzg-1]"
    (forall (p q t)
     (if
      (and (has-continuant-part p q t)
       (instance-of p three-dimensional-spatial-region t))
      (instance-of q spatial-region t))))


  (cl:comment "If a has-continuant-part b then if a is an instance of continuant-fiat-boundary then b is an instance of continuant-fiat-boundary [ixo-1]"
    (forall (p q t)
     (if
      (and (has-continuant-part p q t)
       (instance-of p continuant-fiat-boundary t))
      (instance-of q continuant-fiat-boundary t))))


  (cl:comment "If a continuant-part-of b then if a is an instance of site then b is an instance of site or material-entity  [izr-1]"
    (forall (p q t)
     (if (and (continuant-part-of p q t) (instance-of p site t))
      (or (instance-of q site t) (instance-of q material-entity t)))))


  (cl:comment "If a continuant-part-of b then if a is an instance of independent-continuant then b is an instance of independent-continuant, and vice-versa [cez-1]"
    (forall (p q t)
     (if (continuant-part-of p q t)
      (iff (instance-of p independent-continuant t)
       (and (instance-of q independent-continuant t))))))


  (cl:comment "continuant-part-of is transitive at a time [plp-1]"
    (forall (a b c t t2)
     (if
      (and (continuant-part-of a b t) (continuant-part-of b c t2)
       (temporal-part-of t t2))
      (continuant-part-of a c t))))


  (cl:comment "continuant-part-of is time indexed and has domain: continuant and range: continuant [bdd-1]"
    (forall (a b t)
     (if (continuant-part-of a b t)
      (and (instance-of a continuant t) (instance-of b continuant t)
       (instance-of t temporal-region t)))))


  (cl:comment "If a has-continuant-part b then if a is an instance of fiat-line then b is an instance of fiat-line or fiat-point  [cwp-1]"
    (forall (p q t)
     (if (and (has-continuant-part p q t) (instance-of p fiat-line t))
      (or (instance-of q fiat-line t) (instance-of q fiat-point t)))))


  (cl:comment "If a has-continuant-part b then if a is an instance of site then b is an instance of site or continuant-fiat-boundary  [mjj-1]"
    (forall (p q t)
     (if (and (has-continuant-part p q t) (instance-of p site t))
      (or (instance-of q site t)
       (instance-of q continuant-fiat-boundary t)))))


  (cl:comment "proper-continuant-part-of is time indexed and has domain: continuant and range: continuant [kte-1]"
    (forall (a b t)
     (if (proper-continuant-part-of a b t)
      (and (instance-of a continuant t) (instance-of b continuant t)
       (instance-of t temporal-region t)))))


  (cl:comment "If a has-continuant-part b then if a is an instance of zero-dimensional-spatial-region then b is an instance of zero-dimensional-spatial-region [bfv-1]"
    (forall (p q t)
     (if
      (and (has-continuant-part p q t)
       (instance-of p zero-dimensional-spatial-region t))
      (instance-of q zero-dimensional-spatial-region t))))


  (cl:comment "proper-continuant-part-of is transitive at a time [xpg-1]"
    (forall (a b c t t2)
     (if
      (and (proper-continuant-part-of a b t)
       (proper-continuant-part-of b c t2) (temporal-part-of t t2))
      (proper-continuant-part-of a c t))))


  (cl:comment "A fiat line occupies a one-dimensional spatial region [kcq-1]"
    (forall (x t)
     (if (instance-of x fiat-line t)
      (exists (s tp)
       (and (temporal-part-of tp t) (occupies-spatial-region x s tp)
        (instance-of s one-dimensional-spatial-region tp))))))


  (cl:comment "A fiat point occupies a zero-dimensional spatial region [alm-1]"
    (forall (x t)
     (if (instance-of x fiat-point t)
      (exists (tp s)
       (and (temporal-part-of tp t) (occupies-spatial-region x s tp)
        (instance-of s zero-dimensional-spatial-region tp))))))


  (cl:comment "A fiat surface occupies a two-dimensional spatial region [fpl-1]"
    (forall (x t)
     (if (instance-of x fiat-surface t)
      (exists (s tp)
       (and (temporal-part-of tp t) (occupies-spatial-region x s tp)
        (instance-of s two-dimensional-spatial-region tp))))))


  (cl:comment "If a has-continuant-part b then if a is an instance of material-entity then b is an instance of site or continuant-fiat-boundary or material-entity  [mic-1]"
    (forall (p q t)
     (if
      (and (has-continuant-part p q t) (instance-of p material-entity t))
      (or (instance-of q site t)
       (instance-of q continuant-fiat-boundary t)
       (instance-of q material-entity t)))))


  (cl:comment "If a has-continuant-part b then if a is an instance of one-dimensional-spatial-region then b is an instance of one-dimensional-spatial-region or zero-dimensional-spatial-region  [wne-1]"
    (forall (p q t)
     (if
      (and (has-continuant-part p q t)
       (instance-of p one-dimensional-spatial-region t))
      (or (instance-of q one-dimensional-spatial-region t)
       (instance-of q zero-dimensional-spatial-region t)))))


  (cl:comment "If at all times that two object-aggreates exist each is part of the other, then they are identical [glc-1]"
    (forall (a b)
     (if
      (and
       (exists (t)
        (and (instance-of a object-aggregate t)
         (continuant-part-of a b t) (continuant-part-of b a t)))
       (forall (t)
        (iff (continuant-part-of a b t) (continuant-part-of b a t))))
      (= a b))))


  (cl:comment "The dimensionality of the region of something occupying a one dimensional spatial region does not change [qfe-1]"
    (forall (m s)
     (if
      (exists (t)
       (and (occupies-spatial-region m s t)
        (instance-of s one-dimensional-spatial-region t)))
      (forall (t1 s1)
       (if (occupies-spatial-region m s1 t1)
        (instance-of s1 one-dimensional-spatial-region t1))))))


  (cl:comment "The dimensionality of the region of something occupying a two dimensional spatial region does not change [dor-1]"
    (forall (m s)
     (if
      (exists (t)
       (and (occupies-spatial-region m s t)
        (instance-of s two-dimensional-spatial-region t)))
      (forall (t1 s1)
       (if (occupies-spatial-region m s1 t1)
        (instance-of s1 two-dimensional-spatial-region t1))))))


  (cl:comment "The dimensionality of the region of something occupying a zero dimensional spatial region does not change [fok-1]"
    (forall (m s)
     (if
      (exists (t)
       (and (occupies-spatial-region m s t)
        (instance-of s zero-dimensional-spatial-region t)))
      (forall (t1 s1)
       (if (occupies-spatial-region m s1 t1)
        (instance-of s1 zero-dimensional-spatial-region t1))))))


  (cl:comment "The dimensionality of the region of something occupying a three dimensional spatial region does not change [rlf-1]"
    (forall (m s)
     (if
      (exists (t)
       (and (occupies-spatial-region m s t)
        (instance-of s three-dimensional-spatial-region t)))
      (forall (t1 s1)
       (if (occupies-spatial-region m s1 t1)
        (instance-of s1 three-dimensional-spatial-region t1))))))


  (cl:comment "If a material entity has a proper part, then at least one of its proper parts is not an immaterial entity [adm-1]"
    (forall (m t)
     (if
      (and (instance-of m material-entity t)
       (exists (mp) (and (continuant-part-of mp m t) (not (= mp m)))))
      (exists (mp)
       (and (not (= mp m)) (continuant-part-of mp m t)
        (not (instance-of mp immaterial-entity t)))))))


  (cl:comment "If a has-continuant-part b then if a is an instance of two-dimensional-spatial-region then b is an instance of two-dimensional-spatial-region or one-dimensional-spatial-region or zero-dimensional-spatial-region  [hbn-1]"
    (forall (p q t)
     (if
      (and (has-continuant-part p q t)
       (instance-of p two-dimensional-spatial-region t))
      (or (instance-of q two-dimensional-spatial-region t)
       (instance-of q one-dimensional-spatial-region t)
       (instance-of q zero-dimensional-spatial-region t)))))


  (cl:comment "If at any time that two non-object aggreates exist each is part of the other, then they are identical [tab-1]"
    (forall (a b)
     (if
      (exists (t)
       (and (instance-of a independent-continuant t)
        (not (instance-of a object-aggregate t))
        (instance-of b independent-continuant t)
        (not (instance-of b object-aggregate t))
        (continuant-part-of a b t) (continuant-part-of b a t)))
      (= a b))))


  (cl:comment "continuant-part-of has weak supplementation [fyf-1]"
    (forall (t x y)
     (if
      (and (instance-of x continuant t) (instance-of y continuant t)
       (instance-of t temporal-region t))
      (if (and (continuant-part-of x y t) (not (= x y)))
       (exists (z)
        (and (instance-of z continuant t) (continuant-part-of z y t)
         (not (= z y))
         (not
          (exists (overlap)
           (and (instance-of overlap continuant t)
            (continuant-part-of overlap x t)
            (continuant-part-of overlap z t))))))))))


  (cl:comment "continuant-part-of has a unique product at a time [gzr-1]"
    (forall (x y t)
     (if
      (and (instance-of x continuant t) (instance-of y continuant t)
       (instance-of t temporal-region t))
      (if
       (exists (overlap)
        (and (instance-of overlap continuant t)
         (continuant-part-of overlap x t)
         (continuant-part-of overlap y t)))
       (exists (overlap)
        (and (instance-of overlap continuant t)
         (forall (w)
          (if (instance-of w continuant t)
           (iff (continuant-part-of w overlap t)
            (and (continuant-part-of w x t)
             (continuant-part-of w y t)))))))))))

)))(cl:comment '
BFO 2020 Axiomatization, generated 2024/01/08
The most current version of this file will always be at the GitHub repository https://github.com/bfo-ontology/bfo-2020
Author: Alan Ruttenberg - alanruttenberg(at)gmail.com
This work is licensed under a Creative Commons "Attribution 4.0 International" license: https://creativecommons.org/licenses/by/4.0/'

 (cl:text

  (cl:ttl https://basic-formal-ontology.org/2020/formulas/clif/spatiotemporal.cl

   (cl:outdiscourse occurrent-part-of instance-of occupies-spatial-region located-in occurs-in occupies-spatiotemporal-region spatially-projects-onto temporally-projects-onto temporal-part-of exists-at occupies-temporal-region)

  (cl:comment "If something occupies a temporal region, then it exists at that region [bmc-1]"
    (forall (a t) (if (occupies-temporal-region a t) (exists-at a t))))


  (cl:comment "exists-at is a lower bound on first argument [jqz-1]"
    (forall (p q r)
     (if (and (exists-at p q) (temporal-part-of p r)) (exists-at r q))))


  (cl:comment "occupies-temporal-region is functional on second argument [wzd-1]"
    (forall (p q r)
     (if
      (and (occupies-temporal-region p q) (occupies-temporal-region p r))
      (= q r))))


  (cl:comment "temporally-projects-onto is functional on second argument [jtq-1]"
    (forall (p q r)
     (if
      (and (temporally-projects-onto p q) (temporally-projects-onto p r))
      (= q r))))


  (cl:comment "spatially-projects-onto is functional on second argument [fdb-1]"
    (forall (p q r s)
     (if
      (and (spatially-projects-onto p q r)
       (spatially-projects-onto p s r))
      (= q s))))


  (cl:comment "occupies-spatiotemporal-region is functional on second argument [uqt-1]"
    (forall (p q r)
     (if
      (and (occupies-spatiotemporal-region p q)
       (occupies-spatiotemporal-region p r))
      (= q r))))


  (cl:comment "occurs-in is a lower bound on second argument [yex-1]"
    (forall (p c1 c2)
     (if
      (and (occurs-in p c1)
       (forall (t) (iff (exists-at p t) (located-in c1 c2 t))))
      (occurs-in p c2))))


  (cl:comment "If a occupies-spatial-region b then if a is an instance of site then b is an instance of three-dimensional-spatial-region [uqb-1]"
    (forall (p q t)
     (if (and (occupies-spatial-region p q t) (instance-of p site t))
      (instance-of q three-dimensional-spatial-region t))))


  (cl:comment "The temporal region during which a process occurs is the same as that which the spatiotemporal region the process occupies temporally projects onto [cur-1]"
    (forall (p t)
     (iff (occupies-temporal-region p t)
      (exists (st)
       (and (occupies-spatiotemporal-region p st)
        (temporally-projects-onto st t))))))


  (cl:comment "temporally-projects-onto has domain spatiotemporal-region and range temporal-region [cvr-2]"
    (forall (a b)
     (if (temporally-projects-onto a b)
      (and (exists (t) (instance-of a spatiotemporal-region t))
       (instance-of b temporal-region b)))))


  (cl:comment "If a occupies-spatial-region b then if a is an instance of material-entity then b is an instance of three-dimensional-spatial-region [ocw-1]"
    (forall (p q t)
     (if
      (and (occupies-spatial-region p q t)
       (instance-of p material-entity t))
      (instance-of q three-dimensional-spatial-region t))))


  (cl:comment "A process boundary occupies a spatiotemporal instant [atz-1]"
    (forall (pb tr)
     (if
      (and (exists (t) (instance-of pb process-boundary t))
       (occupies-temporal-region pb tr))
      (instance-of tr temporal-instant tr))))


  (cl:comment "for every process there's a corresponding spatiotemporal-region [qyy-1]"
    (forall (p)
     (if
      (exists (t)
       (or (instance-of p process t) (instance-of p process-boundary t)))
      (exists (s) (occupies-spatiotemporal-region p s)))))


  (cl:comment "Spatiotemporal regions always project on to some temporal region [scq-1]"
    (forall (st)
     (if (exists (t) (instance-of st spatiotemporal-region t))
      (exists (t)
       (and (instance-of t temporal-region t)
        (temporally-projects-onto st t))))))


  (cl:comment "Every temporal region is a projection from a spatiotemporal region [xco-2]"
    (forall (tr)
     (if (instance-of tr temporal-region tr)
      (exists (st)
       (and (exists (t) (instance-of st spatiotemporal-region t))
        (temporally-projects-onto st tr))))))


  (cl:comment "spatially-projects-onto is time indexed and has domain: spatiotemporal-region and range: spatial-region [blj-1]"
    (forall (a b t)
     (if (spatially-projects-onto a b t)
      (and (instance-of a spatiotemporal-region t)
       (instance-of b spatial-region t)
       (instance-of t temporal-region t)))))


  (cl:comment "occupies-temporal-region has domain process or process-boundary  and range temporal-region [lyx-2]"
    (forall (a b)
     (if (occupies-temporal-region a b)
      (and
       (exists (t)
        (or (instance-of a process t)
         (instance-of a process-boundary t)))
       (instance-of b temporal-region b)))))


  (cl:comment "Spatiotemporal regions always project on to some spatial region at any time [geq-1]"
    (forall (st t)
     (if (instance-of st spatiotemporal-region t)
      (exists (s tp)
       (and (temporal-part-of tp t) (instance-of s spatial-region tp)
        (spatially-projects-onto st s tp))))))


  (cl:comment "Every spatial region is a projection from a spatiotemporal region [mdb-1]"
    (forall (sr)
     (if (exists (t) (instance-of sr spatial-region t))
      (exists (st)
       (and (exists (t) (instance-of st spatiotemporal-region t))
        (exists (t) (spatially-projects-onto st sr t)))))))


  (cl:comment "occupies-spatiotemporal-region has domain process or process-boundary  and range spatiotemporal-region [vvo-1]"
    (forall (a b)
     (if (occupies-spatiotemporal-region a b)
      (and
       (exists (t)
        (or (instance-of a process t)
         (instance-of a process-boundary t)))
       (exists (t) (instance-of b spatiotemporal-region t))))))


  (cl:comment "A process occupies at least a temporal interval [fzy-1]"
    (forall (proc tr)
     (if
      (and (exists (t) (instance-of proc process t))
       (occupies-temporal-region proc tr))
      (exists (interval)
       (and (instance-of interval temporal-interval interval)
        (temporal-part-of interval tr))))))


  (cl:comment "If one occurrent is part of another, then the temporal region of the first is part of the temporal region of the second [jiv-1]"
    (forall (o1 o2 t1 t2)
     (if
      (and
       (exists (t)
        (or (instance-of o1 process t)
         (instance-of o1 process-boundary t)))
       (exists (t) (instance-of o2 process t)) (occurrent-part-of o1 o2)
       (occupies-temporal-region o1 t1) (occupies-temporal-region o2 t2))
      (temporal-part-of t1 t2))))


  (cl:comment "If one process or process boundary is part of another, then their corresponding temporal regions are also in a parthood relation [iqe-1]"
    (forall (o1 o2 st1 st2)
     (if
      (and
       (exists (t)
        (or (instance-of o1 process t)
         (instance-of o1 process-boundary t)))
       (exists (t)
        (or (instance-of o2 process t)
         (instance-of o2 process-boundary t)))
       (occurrent-part-of o1 o2) (occupies-spatiotemporal-region o1 st1)
       (occupies-spatiotemporal-region o2 st2))
      (occurrent-part-of st1 st2))))


  (cl:comment "If a process or process boundary is part of another, their spatiotemporal regions are part too [kqv-1]"
    (forall (p1 p2)
     (if
      (and
       (or (exists (t) (instance-of p1 process t))
        (exists (t) (instance-of p1 process-boundary t)))
       (or (exists (t) (instance-of p2 process t))
        (exists (t) (instance-of p2 process-boundary t))))
      (iff (occurrent-part-of p1 p2)
       (exists (st1 st2)
        (and (occupies-spatiotemporal-region p1 st1)
         (occupies-spatiotemporal-region p2 st2)
         (occurrent-part-of st1 st2)))))))


  (cl:comment "process or process-boundary p occupies-temporal-region t iff every part of p temporally occupies a part of t, and there isn't a smaller part of t that p occupies. [tao-1]"
    (forall (o t)
     (if
      (and
       (or (exists (t1) (instance-of o process t1))
        (exists (t1) (instance-of o process-boundary t1)))
       (instance-of t temporal-region t))
      (iff (occupies-temporal-region o t)
       (and
        (forall (op)
         (if (occurrent-part-of op o)
          (forall (tp)
           (if (occupies-temporal-region op tp)
            (occurrent-part-of tp t)))))
        (not
         (exists (tprime)
          (and (not (= tprime t)) (occurrent-part-of tprime t)
           (occupies-temporal-region o tprime)))))))))


  (cl:comment "process p (or boundary) occupies-spatiotemporal-region st iff every part of p  occupies-spatiotemporal-region a part of st, and there isn't a smaller part of st that p occupies. [dki-1]"
    (forall (o st)
     (if
      (and
       (or (exists (t1) (instance-of o process t1))
        (exists (t1) (instance-of o process-boundary t1)))
       (exists (t1) (instance-of st spatiotemporal-region t1)))
      (iff (occupies-spatiotemporal-region o st)
       (and
        (forall (op)
         (if (occurrent-part-of op o)
          (forall (stp)
           (if (occupies-spatiotemporal-region op stp)
            (occurrent-part-of stp st)))))
        (not
         (exists (stprime)
          (and (not (= stprime st)) (occurrent-part-of stprime st)
           (occupies-spatiotemporal-region o stprime)))))))))

)))(cl:comment '
BFO 2020 Axiomatization, generated 2024/01/08
The most current version of this file will always be at the GitHub repository https://github.com/bfo-ontology/bfo-2020
Author: Alan Ruttenberg - alanruttenberg(at)gmail.com
This work is licensed under a Creative Commons "Attribution 4.0 International" license: https://creativecommons.org/licenses/by/4.0/'

 (cl:text

  (cl:ttl https://basic-formal-ontology.org/2020/formulas/clif/order.cl

   (cl:outdiscourse temporally-projects-onto occupies-temporal-region temporal-part-of occurrent-part-of instance-of has-first-instant has-last-instant preceded-by precedes)

  (cl:comment "precedes and preceded-by are inverse relations [tib-1]"
    (forall (a b) (iff (precedes a b) (preceded-by b a))))


  (cl:comment "precedes is antisymmetric [hew-1]"
    (forall (a b) (if (precedes a b) (not (precedes b a)))))


  (cl:comment "precedes is transitive [ctz-1]"
    (forall (a b c)
     (if (and (precedes a b) (precedes b c)) (precedes a c))))


  (cl:comment "If the last instant of a temporal region precedes the first instant of another, then the first region precedes the second [qqv-1]"
    (forall (i1 i2 l1 f2)
     (if
      (and (has-last-instant i1 l1) (has-first-instant i2 f2)
       (precedes l1 f2))
      (precedes i1 i2))))


  (cl:comment "precedes has domain occurrent and range occurrent [sen-1]"
    (forall (a b)
     (if (precedes a b)
      (and (exists (t) (instance-of a occurrent t))
       (exists (t) (instance-of b occurrent t))))))


  (cl:comment "If you are part of something that precedes something else, you also precede it [wix-1]"
    (forall (o1 o2 o1p o2p)
     (if
      (and (occurrent-part-of o1p o1) (occurrent-part-of o2p o2)
       (precedes o1 o2))
      (precedes o1p o2p))))


  (cl:comment "First instant of a temporal region that is not an instant precedes last instant [rzv-1]"
    (forall (t ft lt)
     (if
      (and (not (instance-of t temporal-instant t))
       (has-first-instant t ft) (has-last-instant t lt))
      (precedes ft lt))))


  (cl:comment "If one temporal region precedes another then the first last time point precedes the second first time point [miz-1]"
    (forall (t1 t2 l1 f2)
     (if
      (and (precedes t1 t2) (has-last-instant t1 l1)
       (has-first-instant t2 f2) (not (= l1 f2)))
      (precedes l1 f2))))


  (cl:comment "if one occurrent precedes another then they do not overlap temporally [aou-1]"
    (forall (p q)
     (if (or (precedes p q) (precedes q p))
      (not
       (exists (overlap)
        (and (temporal-part-of overlap p)
         (temporal-part-of overlap q)))))))


  (cl:comment "temporal instants are totally ordered [qnf-1]"
    (forall (t1 t2)
     (if
      (and (instance-of t1 temporal-instant t1)
       (instance-of t2 temporal-instant t2))
      (or (precedes t1 t2) (precedes t2 t1) (= t1 t2)))))


  (cl:comment "If the last instant of a temporal region is the first instant of another, the first region precedes the second [suk-1]"
    (forall (i1 i2 l1 f2)
     (if
      (and (not (instance-of i1 temporal-instant i1))
       (not (instance-of i2 temporal-instant i2))
       (has-last-instant i1 l1) (has-first-instant i2 f2) (= l1 f2))
      (precedes i1 i2))))


  (cl:comment "A last instant is either part of an extended region or is preceded by it [acg-1]"
    (forall (l i)
     (if
      (and (instance-of l temporal-instant l)
       (instance-of i temporal-region i)
       (not (instance-of i temporal-instant i)) (has-last-instant i l))
      (iff (not (temporal-part-of l i)) (precedes i l)))))


  (cl:comment "A first instant is either part of an extended region or precedes it [qga-1]"
    (forall (f i)
     (if
      (and (instance-of f temporal-instant f)
       (instance-of i temporal-region i)
       (not (instance-of i temporal-instant i)) (has-first-instant i f))
      (iff (not (temporal-part-of f i)) (precedes f i)))))


  (cl:comment "If two temporal intervals do not overlap then one of them precedes the other [owb-1]"
    (forall (t1 t2)
     (if
      (and (instance-of t1 temporal-interval t1)
       (instance-of t2 temporal-interval t2)
       (not
        (exists (part)
         (and (temporal-part-of part t1) (temporal-part-of part t2)))))
      (or (precedes t1 t2) (precedes t2 t1)))))


  (cl:comment "If you temporally occupy part of something that precedes something else, you also precede it [wff-1]"
    (forall (o1 o2)
     (iff
      (exists (t1 t2)
       (and
        (or (occupies-temporal-region o1 t1)
         (temporally-projects-onto o1 t1) (= t1 o1))
        (or (occupies-temporal-region o2 t2)
         (temporally-projects-onto o2 t2) (= t2 o2))
        (precedes t1 t2)))
      (precedes o1 o2))))


  (cl:comment "If two processes that occupy temporal intervals do not overlap, one of them precedes the other [duz-1]"
    (forall (o1 o2 t1 t2)
     (if
      (and (occupies-temporal-region o1 t1)
       (occupies-temporal-region o2 t2)
       (instance-of t1 temporal-interval t1)
       (instance-of t2 temporal-interval t2)
       (not
        (exists (part)
         (and (temporal-part-of part t1) (temporal-part-of part t2)))))
      (or (precedes o1 o2) (precedes o2 o1)))))

)))(cl:comment '
BFO 2020 Axiomatization, generated 2024/01/08
The most current version of this file will always be at the GitHub repository https://github.com/bfo-ontology/bfo-2020
Author: Alan Ruttenberg - alanruttenberg(at)gmail.com
This work is licensed under a Creative Commons "Attribution 4.0 International" license: https://creativecommons.org/licenses/by/4.0/'

 (cl:text

  (cl:ttl https://basic-formal-ontology.org/2020/formulas/clif/spatial.cl

   (cl:outdiscourse instance-of spatially-projects-onto occupies-spatial-region continuant-part-of temporal-part-of exists-at occurrent-part-of location-of located-in environs occurs-in)

  (cl:comment "occurs-in and environs are inverse relations [uys-1]"
    (forall (a b) (iff (occurs-in a b) (environs b a))))


  (cl:comment "located-in and location-of are inverse relations [kaw-1]"
    (forall (t a b) (iff (located-in a b t) (location-of b a t))))


  (cl:comment "occurs-in is dissective on first argumentwhen it is an occurrent [jil-1]"
    (forall (p q r)
     (if (and (occurs-in p q) (occurrent-part-of r p)) (occurs-in r q))))


  (cl:comment "If a process (or process-boundary) occurs in a continuant, that continuant exists at least as long as the process does [dxv-1]"
    (forall (p c)
     (if (occurs-in p c)
      (forall (t) (if (exists-at p t) (exists-at c t))))))


  (cl:comment "located-in is dissective on third argument, a temporal region [put-1]"
    (forall (p q r s)
     (if (and (located-in p q r) (temporal-part-of s r))
      (located-in p q s))))


  (cl:comment "located-in is a lower bound on second argument [evu-1]"
    (forall (p q r s)
     (if (and (located-in p q r) (continuant-part-of q s r))
      (located-in p s r))))


  (cl:comment "located-in is dissective on first argumentwhen it is a continuant [wty-1]"
    (forall (p q r s)
     (if (and (located-in p q r) (continuant-part-of s p r))
      (located-in s q r))))


  (cl:comment "occupies-spatial-region is functional on second argument [zls-1]"
    (forall (p q r s)
     (if
      (and (occupies-spatial-region p q r)
       (occupies-spatial-region p s r))
      (= q s))))


  (cl:comment "occupies-spatial-region is dissective on third argument, a temporal region [mud-1]"
    (forall (p q r s)
     (if (and (occupies-spatial-region p q r) (temporal-part-of s r))
      (occupies-spatial-region p q s))))


  (cl:comment "spatially-projects-onto is dissective on third argument, a temporal region [ivt-1]"
    (forall (p q r s)
     (if (and (spatially-projects-onto p q r) (temporal-part-of s r))
      (spatially-projects-onto p q s))))


  (cl:comment "located-in is transitive at a time [ets-1]"
    (forall (a b c t t2)
     (if
      (and (located-in a b t) (located-in b c t2)
       (temporal-part-of t t2))
      (located-in a c t))))


  (cl:comment "If a location-of b then if a is an instance of continuant-fiat-boundary then b is an instance of continuant-fiat-boundary [wte-1]"
    (forall (p q t)
     (if
      (and (location-of p q t)
       (instance-of p continuant-fiat-boundary t))
      (instance-of q continuant-fiat-boundary t))))


  (cl:comment "All spatial regions are part of a 3-dimensional spatial region [xcx-1]"
    (forall (s t)
     (if (instance-of s spatial-region t)
      (exists (s3)
       (and (instance-of s3 three-dimensional-spatial-region t)
        (continuant-part-of s s3 t))))))


  (cl:comment "occurs-in is lower bound location [czc-1]"
    (forall (p c1 c2)
     (if
      (and (occurs-in p c1)
       (forall (t)
        (iff (exists-at p t)
         (and (exists-at c2 t) (continuant-part-of c1 c2 t)))))
      (occurs-in p c2))))


  (cl:comment "If something is located in something else then the region of the first is part of the region of the second [uas-1]"
    (forall (a b t)
     (if (located-in a b t)
      (exists (r1 r2 t2)
       (and (temporal-part-of t2 t) (occupies-spatial-region a r1 t2)
        (occupies-spatial-region b r2 t2)
        (continuant-part-of r1 r2 t2))))))


  (cl:comment "occurs-in has domain process or process-boundary  and range material-entity or site  [tfw-1]"
    (forall (a b)
     (if (occurs-in a b)
      (and
       (exists (t)
        (or (instance-of a process t)
         (instance-of a process-boundary t)))
       (exists (t)
        (or (instance-of b material-entity t) (instance-of b site t)))))))


  (cl:comment "spatial regions don't change what they are part of. [mlb-1]"
    (forall (s sp)
     (if
      (exists (t)
       (and (instance-of s spatial-region t)
        (continuant-part-of sp s t)))
      (forall (t)
       (if (exists (s-prime) (continuant-part-of s-prime s t))
        (continuant-part-of sp s t))))))


  (cl:comment "occupies-spatial-region is time indexed and has domain: independent-continuant but not spatial-region and range: spatial-region [lzw-1]"
    (forall (a b t)
     (if (occupies-spatial-region a b t)
      (and
       (and (instance-of a independent-continuant t)
        (not (instance-of a spatial-region t)))
       (instance-of b spatial-region t)
       (instance-of t temporal-region t)))))


  (cl:comment "If there are two independent continuants that are not spatial regions, and one is part of the other, then it is located in the other [bao-1]"
    (forall (a b t)
     (if
      (and (continuant-part-of a b t)
       (instance-of a independent-continuant t)
       (not (instance-of a spatial-region t))
       (instance-of b independent-continuant t)
       (not (instance-of b spatial-region t)))
      (located-in a b t))))


  (cl:comment "spatial-region is the union of zero-dimensional-spatial-region, one-dimensional-spatial-region, two-dimensional-spatial-region, and three-dimensional-spatial-region  [wnm-1]"
    (forall (i t)
     (if (instance-of i spatial-region t)
      (or (instance-of i zero-dimensional-spatial-region t)
       (instance-of i one-dimensional-spatial-region t)
       (instance-of i two-dimensional-spatial-region t)
       (instance-of i three-dimensional-spatial-region t)))))


  (cl:comment "No two material entities occupy the same space unless they coincide [scr-1]"
    (forall (m1 m2 s t)
     (if
      (and (instance-of m1 material-entity t)
       (occupies-spatial-region m1 s t)
       (instance-of m2 material-entity t)
       (occupies-spatial-region m2 s t))
      (or (and (continuant-part-of m2 m1 t) (continuant-part-of m1 m2 t))
       (= m1 m2)))))


  (cl:comment "located-in is time indexed and has domain: independent-continuant but not spatial-region and range: independent-continuant but not spatial-region [bge-1]"
    (forall (a b t)
     (if (located-in a b t)
      (and
       (and (instance-of a independent-continuant t)
        (not (instance-of a spatial-region t)))
       (and (instance-of b independent-continuant t)
        (not (instance-of b spatial-region t)))
       (instance-of t temporal-region t)))))


  (cl:comment "at all times t, there's a part of t when c occupies-spatial-region r iff every part of c occupies a part of r, and there isn't a smaller part of r that c occupies. [grv-1]"
    (forall (c r t)
     (if
      (and (instance-of c independent-continuant t)
       (not (instance-of c spatial-region t))
       (instance-of r spatial-region t))
      (exists (t2)
       (and (temporal-part-of t2 t)
        (iff (occupies-spatial-region c r t2)
         (and
          (forall (cp)
           (if (continuant-part-of cp c t2)
            (forall (rp)
             (if (occupies-spatial-region cp rp t2)
              (continuant-part-of rp r t2)))))
          (not
           (exists (rprime)
            (and (not (= rprime r)) (continuant-part-of rprime r t2)
             (occupies-spatial-region c rprime t2)))))))))))

)))(cl:comment '
BFO 2020 Axiomatization, generated 2024/01/08
The most current version of this file will always be at the GitHub repository https://github.com/bfo-ontology/bfo-2020
Author: Alan Ruttenberg - alanruttenberg(at)gmail.com
This work is licensed under a Creative Commons "Attribution 4.0 International" license: https://creativecommons.org/licenses/by/4.0/'

 (cl:text

  (cl:ttl https://basic-formal-ontology.org/2020/formulas/clif/specific-dependency.cl

   (cl:outdiscourse exists-at has-first-instant occupies-temporal-region continuant-part-of instance-of temporal-part-of participates-in specifically-depended-on-by specifically-depends-on material-basis-of has-material-basis has-realization realizes bearer-of inheres-in)

  (cl:comment "inheres-in and bearer-of are inverse relations [dzz-1]"
    (forall (a b) (iff (inheres-in a b) (bearer-of b a))))


  (cl:comment "realizes and has-realization are inverse relations [pvk-1]"
    (forall (a b) (iff (realizes a b) (has-realization b a))))


  (cl:comment "has-material-basis and material-basis-of are inverse relations [tla-1]"
    (forall (t a b)
     (iff (has-material-basis a b t) (material-basis-of b a t))))


  (cl:comment "specifically-depends-on and specifically-depended-on-by are inverse relations [yct-1]"
    (forall (a b)
     (iff (specifically-depends-on a b)
      (specifically-depended-on-by b a))))


  (cl:comment "When a role is realized the bearer of the role participates in the realization process [grx-1]"
    (forall (r p b)
     (if (and (realizes p r) (inheres-in r b))
      (exists (t) (participates-in b p t)))))


  (cl:comment "has-material-basis is dissective on third argument, a temporal region [hnl-1]"
    (forall (p q r s)
     (if (and (has-material-basis p q r) (temporal-part-of s r))
      (has-material-basis p q s))))


  (cl:comment "realizes has domain process and range realizable-entity [oot-1]"
    (forall (a b)
     (if (realizes a b)
      (and (exists (t) (instance-of a process t))
       (exists (t) (instance-of b realizable-entity t))))))


  (cl:comment "specifically-depends-on is transitive [myu-1]"
    (forall (a b c)
     (if
      (and (specifically-depends-on a b) (specifically-depends-on b c)
       (not (= a c)))
      (specifically-depends-on a c))))


  (cl:comment "if s s-depends_on c then s and c never share common parts (s,c continuants) [nfe-1]"
    (forall (s c)
     (if (specifically-depends-on s c)
      (not
       (exists (w t)
        (and (continuant-part-of w s t) (continuant-part-of w c t)))))))


  (cl:comment "A realizable entity exists at least at the beginning of the realization process [vhg-1]"
    (forall (r p)
     (if (realizes p r)
      (exists (proct first)
       (and (occupies-temporal-region p proct)
        (has-first-instant proct first) (exists-at r first))))))


  (cl:comment "has-material-basis is time indexed and has domain: disposition and range: material-entity [cfs-1]"
    (forall (a b t)
     (if (has-material-basis a b t)
      (and (instance-of a disposition t)
       (instance-of b material-entity t)
       (instance-of t temporal-region t)))))


  (cl:comment "If s s-depends-on c then there's at least one time when they both exist and whenever s exists, c must also exist [iyu-1]"
    (forall (s c)
     (if (specifically-depends-on s c)
      (and (exists (t) (and (exists-at s t) (exists-at c t)))
       (forall (t) (if (exists-at s t) (exists-at c t)))))))


  (cl:comment "No role changes type during its existence [bks-1]"
    (forall (o)
     (if (exists (t) (instance-of o role t))
      (forall (u)
       (if (exists (t) (instance-of o u t))
        (forall (t) (iff (instance-of o role t) (instance-of o u t))))))))


  (cl:comment "DEFINITION: b is a relational quality = Def. b is a quality and there exists distinct c and d such that at all times t, b inheres in c if and only b specifically-depends-on. [dbp-1]"
    (forall (b)
     (iff (exists (t) (instance-of b relational-quality t))
      (and
       (exists (c d)
        (and (not (= c d)) (inheres-in b c)
         (specifically-depends-on b d)))
       (exists (t) (instance-of b quality t))))))


  (cl:comment "a inheres_in b =Def. a is a specifically dependent continuant and b is an independent continuant that is not a spatial region and a s-depends_on b. [tht-1]"
    (forall (a b)
     (iff (inheres-in a b)
      (and (specifically-depends-on a b)
       (exists (t)
        (and (instance-of a specifically-dependent-continuant t)
         (instance-of b independent-continuant t)
         (not (instance-of b spatial-region t))))))))


  (cl:comment "Definition of specifically dependent continuant. [akq-1]"
    (forall (s)
     (iff
      (exists (t) (instance-of s specifically-dependent-continuant t))
      (exists (c t)
       (and (instance-of s continuant t)
        (instance-of c independent-continuant t)
        (not (instance-of c spatial-region t))
        (specifically-depends-on s c))))))


  (cl:comment "The material basis of a disposition is part of the bearer of the disposition [uxo-1]"
    (forall (m d b)
     (if
      (and (exists (t) (instance-of m material-entity t))
       (exists (t) (instance-of d disposition t))
       (exists (t) (instance-of b material-entity t)) (inheres-in d b))
      (forall (t)
       (if (has-material-basis d m t) (continuant-part-of m b t))))))


  (cl:comment "specifically-depends-on has domain specifically-dependent-continuant and range specifically-dependent-continuant or independent-continuant but not spatial-region  [kkl-1]"
    (forall (a b)
     (if (specifically-depends-on a b)
      (and
       (exists (t) (instance-of a specifically-dependent-continuant t))
       (exists (t)
        (or (instance-of b specifically-dependent-continuant t)
         (and (instance-of b independent-continuant t)
          (not (instance-of b spatial-region t)))))))))


  (cl:comment "At every time a specific dependent s participates in a process p there's a part of that time, during which there's an independent-continuant that s s-depends on, and that participates in p at that time [cgn-1]"
    (forall (sdc p t)
     (if
      (and (instance-of sdc specifically-dependent-continuant t)
       (participates-in sdc p t))
      (exists (tp ic)
       (and (instance-of tp temporal-region tp) (temporal-part-of tp t)
        (instance-of ic independent-continuant tp)
        (not (instance-of ic spatial-region tp))
        (specifically-depends-on sdc ic) (participates-in ic p tp))))))

)))(cl:comment '
BFO 2020 Axiomatization, generated 2024/01/08
The most current version of this file will always be at the GitHub repository https://github.com/bfo-ontology/bfo-2020
Author: Alan Ruttenberg - alanruttenberg(at)gmail.com
This work is licensed under a Creative Commons "Attribution 4.0 International" license: https://creativecommons.org/licenses/by/4.0/'

 (cl:text

  (cl:ttl https://basic-formal-ontology.org/2020/formulas/clif/temporal-region.cl

   (cl:outdiscourse precedes has-proper-temporal-part proper-temporal-part-of instance-of occurrent-part-of has-temporal-part temporal-part-of first-instant-of has-first-instant last-instant-of has-last-instant)

  (cl:comment "has-last-instant and last-instant-of are inverse relations [wal-1]"
    (forall (a b) (iff (has-last-instant a b) (last-instant-of b a))))


  (cl:comment "has-first-instant and first-instant-of are inverse relations [bon-1]"
    (forall (a b) (iff (has-first-instant a b) (first-instant-of b a))))


  (cl:comment "temporal-part-of and has-temporal-part are inverse relations [boo-1]"
    (forall (a b) (iff (temporal-part-of a b) (has-temporal-part b a))))


  (cl:comment "temporal-part-of for occurrents implies occurrent-part-of [bal-1]"
    (forall (a b) (if (temporal-part-of a b) (occurrent-part-of a b))))


  (cl:comment "temporal-part-of is reflexive [dbj-2]"
    (forall (a)
     (if (instance-of a temporal-region a) (temporal-part-of a a))))


  (cl:comment "proper-temporal-part-of and has-proper-temporal-part are inverse relations [dbc-1]"
    (forall (a b)
     (iff (proper-temporal-part-of a b) (has-proper-temporal-part b a))))


  (cl:comment "If something is an instance of temporal region at t, then t is part of that temporal region [njq-1]"
    (forall (ti t)
     (if (instance-of ti temporal-region t) (temporal-part-of t ti))))


  (cl:comment "temporal-part-of is reflexive [bvr-1]"
    (forall (a)
     (if (exists (t) (instance-of a occurrent t)) (temporal-part-of a a))))


  (cl:comment "temporal-part-of is antisymmetric [zdq-1]"
    (forall (a b)
     (if (and (temporal-part-of a b) (temporal-part-of b a)) (= a b))))


  (cl:comment "proper-temporal-part-of is asymmetric [aqu-1]"
    (forall (a b)
     (if (proper-temporal-part-of a b)
      (not (proper-temporal-part-of b a)))))


  (cl:comment "has-last-instant is functional on second argument [ogd-1]"
    (forall (p q r)
     (if (and (has-last-instant p q) (has-last-instant p r)) (= q r))))


  (cl:comment "has-first-instant is functional on second argument [fwf-1]"
    (forall (p q r)
     (if (and (has-first-instant p q) (has-first-instant p r)) (= q r))))


  (cl:comment "a proper temporal part of b means a is a temporal part of b and b a is not the same as b [aeu-1]"
    (forall (x y)
     (iff (proper-temporal-part-of x y)
      (and (temporal-part-of x y) (not (= x y))))))


  (cl:comment "The only part of a temporal instant is itself [pir-2]"
    (forall (p q)
     (if (and (instance-of p temporal-instant p) (has-temporal-part p q))
      (= p q))))


  (cl:comment "instance-of is dissective on third argument, a temporal region [qaf-1]"
    (forall (p q r s)
     (if (and (instance-of p q r) (temporal-part-of s r))
      (instance-of p q s))))


  (cl:comment "temporal-part-of is transitive [bfq-1]"
    (forall (a b c)
     (if (and (temporal-part-of a b) (temporal-part-of b c))
      (temporal-part-of a c))))


  (cl:comment "The first and last time points for an instant are the instant itself [nfo-1]"
    (forall (i)
     (iff (instance-of i temporal-instant i)
      (and (has-first-instant i i) (has-last-instant i i)))))


  (cl:comment "temporal regions are instances at themselves [tvx-2]"
    (forall (a u)
     (iff
      (exists (t)
       (and (instance-of a temporal-region t) (instance-of a u t)))
      (instance-of a u a))))


  (cl:comment "If a temporal-part-of b then if a is an instance of temporal-region then b is an instance of temporal-region, and vice-versa [mjn-2]"
    (forall (p q)
     (if (temporal-part-of p q)
      (iff (instance-of p temporal-region p)
       (instance-of q temporal-region q)))))


  (cl:comment "has-last-instant has domain temporal-region and range temporal-instant [jtk-2]"
    (forall (a b)
     (if (has-last-instant a b)
      (and (instance-of a temporal-region a)
       (instance-of b temporal-instant b)))))


  (cl:comment "proper-temporal-part-of is transitive [mns-1]"
    (forall (a b c)
     (if
      (and (proper-temporal-part-of a b) (proper-temporal-part-of b c))
      (proper-temporal-part-of a c))))


  (cl:comment "has-first-instant has domain temporal-region and range temporal-instant [fwk-2]"
    (forall (a b)
     (if (has-first-instant a b)
      (and (instance-of a temporal-region a)
       (instance-of b temporal-instant b)))))


  (cl:comment "If the last instant of a temporal region precedes the first instant of another, then the first region precedes the second [qqv-1]"
    (forall (i1 i2 l1 f2)
     (if
      (and (has-last-instant i1 l1) (has-first-instant i2 f2)
       (precedes l1 f2))
      (precedes i1 i2))))


  (cl:comment "any temporal region has a first and last instant [daf-1]"
    (forall (i)
     (if (instance-of i temporal-region i)
      (exists (t1 t2)
       (and (has-first-instant i t1) (has-last-instant i t2))))))


  (cl:comment "All temporal regions are part of a temporal interval [mvd-1]"
    (forall (t)
     (if (instance-of t temporal-region t)
      (exists (i)
       (and (instance-of i temporal-interval i) (temporal-part-of t i))))))


  (cl:comment "temporal-part-of has domain occurrent and range occurrent [ruj-1]"
    (forall (a b)
     (if (temporal-part-of a b)
      (and (exists (t) (instance-of a occurrent t))
       (exists (t) (instance-of b occurrent t))))))


  (cl:comment "First instant of a temporal region that is not an instant precedes last instant [rzv-1]"
    (forall (t ft lt)
     (if
      (and (not (instance-of t temporal-instant t))
       (has-first-instant t ft) (has-last-instant t lt))
      (precedes ft lt))))


  (cl:comment "If one temporal region precedes another then the first last time point precedes the second first time point [miz-1]"
    (forall (t1 t2 l1 f2)
     (if
      (and (precedes t1 t2) (has-last-instant t1 l1)
       (has-first-instant t2 f2) (not (= l1 f2)))
      (precedes l1 f2))))


  (cl:comment "If a temporal-part-of b then if a is an instance of one-dimensional-temporal-region then b is an instance of one-dimensional-temporal-region [mei-2]"
    (forall (p q)
     (if (temporal-part-of p q)
      (if (instance-of p one-dimensional-temporal-region p)
       (instance-of q one-dimensional-temporal-region q)))))


  (cl:comment "A one-dimensional temporal region has at least one interval as part [jhe-1]"
    (forall (t)
     (if (and (instance-of t one-dimensional-temporal-region t))
      (exists (p)
       (and (temporal-part-of p t) (instance-of p temporal-interval p))))))


  (cl:comment "If a has-temporal-part b then if a is an instance of zero-dimensional-temporal-region then b is an instance of zero-dimensional-temporal-region [bnt-2]"
    (forall (p q)
     (if (has-temporal-part p q)
      (if (instance-of p zero-dimensional-temporal-region p)
       (instance-of q zero-dimensional-temporal-region q)))))


  (cl:comment "temporal instants are totally ordered [qnf-1]"
    (forall (t1 t2)
     (if
      (and (instance-of t1 temporal-instant t1)
       (instance-of t2 temporal-instant t2))
      (or (precedes t1 t2) (precedes t2 t1) (= t1 t2)))))


  (cl:comment "temporal-region is the union of zero-dimensional-temporal-region and one-dimensional-temporal-region  [hgs-1]"
    (forall (i t)
     (if (instance-of i temporal-region t)
      (or (instance-of i zero-dimensional-temporal-region t)
       (instance-of i one-dimensional-temporal-region t)))))


  (cl:comment "If the last instant of a temporal region is the first instant of another, the first region precedes the second [suk-1]"
    (forall (i1 i2 l1 f2)
     (if
      (and (not (instance-of i1 temporal-instant i1))
       (not (instance-of i2 temporal-instant i2))
       (has-last-instant i1 l1) (has-first-instant i2 f2) (= l1 f2))
      (precedes i1 i2))))


  (cl:comment "If a has-temporal-part b then if a is an instance of one-dimensional-temporal-region then b is an instance of one-dimensional-temporal-region or zero-dimensional-temporal-region  [eeg-2]"
    (forall (p q)
     (if (has-temporal-part p q)
      (if (instance-of p one-dimensional-temporal-region p)
       (or (instance-of q one-dimensional-temporal-region q)
        (instance-of q zero-dimensional-temporal-region q))))))


  (cl:comment "A last instant is either part of an extended region or is preceded by it [acg-1]"
    (forall (l i)
     (if
      (and (instance-of l temporal-instant l)
       (instance-of i temporal-region i)
       (not (instance-of i temporal-instant i)) (has-last-instant i l))
      (iff (not (temporal-part-of l i)) (precedes i l)))))


  (cl:comment "A first instant is either part of an extended region or precedes it [qga-1]"
    (forall (f i)
     (if
      (and (instance-of f temporal-instant f)
       (instance-of i temporal-region i)
       (not (instance-of i temporal-instant i)) (has-first-instant i f))
      (iff (not (temporal-part-of f i)) (precedes f i)))))


  (cl:comment "If two temporal intervals do not overlap then one of them precedes the other [owb-1]"
    (forall (t1 t2)
     (if
      (and (instance-of t1 temporal-interval t1)
       (instance-of t2 temporal-interval t2)
       (not
        (exists (part)
         (and (temporal-part-of part t1) (temporal-part-of part t2)))))
      (or (precedes t1 t2) (precedes t2 t1)))))


  (cl:comment "The first temporal instant is such that it precedes every part of the interval that doesn't have the first instant as part [ixz-1]"
    (forall (fi i)
     (if
      (and (instance-of fi temporal-instant fi)
       (instance-of i temporal-region i)
       (not (instance-of i temporal-instant i)))
      (if (has-first-instant i fi)
       (forall (ip)
        (if (and (temporal-part-of ip i) (not (temporal-part-of fi ip)))
         (precedes fi ip)))))))


  (cl:comment "The last temporal instant is such that every part of the interval that doesn't have the last instant as part precedes it [nhd-1]"
    (forall (li i)
     (if
      (and (instance-of li temporal-instant li)
       (instance-of i temporal-region i)
       (not (instance-of i temporal-instant i)))
      (if (has-last-instant i li)
       (and
        (forall (ip)
         (if (and (temporal-part-of ip i) (not (temporal-part-of li ip)))
          (precedes ip li))))))))


  (cl:comment "intervals have no internal gaps [ekm-1]"
    (forall (i start end)
     (if
      (and (instance-of i temporal-interval i)
       (has-first-instant i start) (has-last-instant i end))
      (not
       (exists (gap gap-start gap-end)
        (and (has-first-instant gap gap-start)
         (has-last-instant gap gap-end) (precedes gap-end end)
         (precedes start gap-start) (not (temporal-part-of gap i))))))))


  (cl:comment "temporal-part-of has weak-supplementation [vbw-1]"
    (forall (x y)
     (if
      (and (instance-of x temporal-region x)
       (instance-of y temporal-region y))
      (if (proper-temporal-part-of x y)
       (exists (z)
        (and (proper-temporal-part-of z y)
         (not
          (exists (overlap)
           (and (instance-of overlap temporal-region overlap)
            (temporal-part-of overlap x)
            (temporal-part-of overlap z))))))))))


  (cl:comment "any temporal instant that precedes the last instant of an interval and which is preceded by the first instant is part of the interval [zlp-1]"
    (forall (t r)
     (if
      (and (instance-of t temporal-instant t)
       (instance-of r temporal-interval r))
      (or (has-first-instant r t) (has-last-instant r t)
       (iff
        (exists (f l)
         (and (instance-of r temporal-interval r) (has-first-instant r f)
          (has-last-instant r l) (precedes t l) (precedes f t)))
        (proper-temporal-part-of t r))))))


  (cl:comment "two intervals are identical if their first and last instants are the same and if an instant is part of one of the intervals it is also part of the other [xkl-1]"
    (forall (i1 i2)
     (if
      (and (instance-of i1 temporal-interval i1)
       (instance-of i2 temporal-interval i2))
      (if
       (exists (f l)
        (and (has-first-instant i1 f) (has-first-instant i2 f)
         (has-last-instant i1 l) (has-last-instant i2 l)
         (iff (temporal-part-of l i1) (temporal-part-of l i2))
         (iff (temporal-part-of f i1) (temporal-part-of f i2))))
       (= i1 i2)))))


  (cl:comment "temporal-part-of has unique-product [wsg-2]"
    (forall (x y)
     (if
      (and (instance-of x temporal-region x)
       (instance-of y temporal-region y))
      (if
       (exists (o) (and (temporal-part-of o x) (temporal-part-of o y)))
       (exists (z)
        (and (instance-of z temporal-region z)
         (forall (w)
          (if
           (and (instance-of w temporal-region w)
            (instance-of z temporal-region z))
           (iff (temporal-part-of w z)
            (and (temporal-part-of w x) (temporal-part-of w y)))))))))))


  (cl:comment "An interval has no gaps [nui-1]"
    (forall (i start end)
     (if
      (and (instance-of i temporal-interval i)
       (has-first-instant i start) (has-last-instant i end))
      (not
       (exists (gap gap-start gap-end)
        (and (not (instance-of gap temporal-instant gap))
         (has-first-instant gap gap-start) (has-last-instant gap gap-end)
         (or (precedes gap-end end)
          (and (temporal-part-of end i) (= gap-end end)))
         (or (precedes start gap-start)
          (and (temporal-part-of start i) (= gap-start start)))
         (not (temporal-part-of gap i))))))))


  (cl:comment "intervals have no gaps - strong version - every two instants without another in between bound an interval [cop-1]"
    (forall (i start end)
     (if
      (and (instance-of i temporal-interval i)
       (has-first-instant i start) (has-last-instant i end))
      (forall (t1 t2)
       (if
        (and (temporal-part-of t1 i) (temporal-part-of t2 i)
         (instance-of t1 temporal-instant t1)
         (instance-of t2 temporal-instant t2) (precedes t1 t2)
         (not
          (exists (t3)
           (and (instance-of t3 temporal-instant t3) (precedes t1 t3)
            (precedes t3 t2)))))
        (exists (fill)
         (and (instance-of fill temporal-interval fill)
          (has-first-instant fill t1) (has-last-instant fill t2)
          (temporal-part-of fill i))))))))

)))(cl:comment '
BFO 2020 Axiomatization, generated 2024/01/08
The most current version of this file will always be at the GitHub repository https://github.com/bfo-ontology/bfo-2020
Author: Alan Ruttenberg - alanruttenberg(at)gmail.com
This work is licensed under a Creative Commons "Attribution 4.0 International" license: https://creativecommons.org/licenses/by/4.0/'

 (cl:text

  (cl:ttl https://basic-formal-ontology.org/2020/formulas/clif/existence-instantiation.cl

   (cl:outdiscourse temporal-part-of continuant-part-of instance-of universal exists-at particular)

  (cl:comment "Particulars exist at some time [nmq-1]"
    (forall (p) (if (particular p) (exists (t) (exists-at p t)))))


  (cl:comment "Every universal is instantiated at least once [mbf-1]"
    (forall (u) (if (universal u) (exists (p t) (instance-of p u t)))))


  (cl:comment "exists-at is dissective on first argument when it is a continuant [uns-1]"
    (forall (p q r)
     (if (and (exists-at p q) (continuant-part-of r p q))
      (exists-at r q))))


  (cl:comment "instance-of is dissective on third argument, a temporal region [qaf-1]"
    (forall (p q r s)
     (if (and (instance-of p q r) (temporal-part-of s r))
      (instance-of p q s))))


  (cl:comment "Relata of exists-at are particulars. [oap-1]"
    (forall (i t)
     (if (exists-at i t)
      (and (particular i) (particular t)
       (instance-of t temporal-region t)))))


  (cl:comment "Relata of instance-of are particular, universal, temporal-region. [lqn-1]"
    (forall (i u t)
     (if (instance-of i u t)
      (and (particular i) (universal u)
       (instance-of t temporal-region t)))))


  (cl:comment "There is always something that exists [nis-1]"
    (forall (t)
     (if (instance-of t temporal-region t)
      (exists (u i)
       (and (not (= i t)) (universal u) (particular i)
        (instance-of i u t))))))


  (cl:comment "if m is a material entity, then there is some one-dimensional temporal region during which m exists [zuw-1]"
    (forall (m)
     (if (exists (t) (instance-of m material-entity t))
      (exists (t)
       (and (instance-of t one-dimensional-temporal-region t)
        (exists-at m t))))))


  (cl:comment "If you exist you instatiate a universal and vice-versa [bee-1]"
    (forall (a t)
     (iff
      (exists (u)
       (and (universal u) (instance-of a u t)
        (instance-of t temporal-region t)))
      (and (particular a) (instance-of t temporal-region t)
       (exists-at a t)))))

)))(cl:comment '
BFO 2020 Axiomatization, generated 2024/01/08
The most current version of this file will always be at the GitHub repository https://github.com/bfo-ontology/bfo-2020
Author: Alan Ruttenberg - alanruttenberg(at)gmail.com
This work is licensed under a Creative Commons "Attribution 4.0 International" license: https://creativecommons.org/licenses/by/4.0/'

 (cl:text

  (cl:ttl https://basic-formal-ontology.org/2020/formulas/clif/material-entity.cl

   (cl:outdiscourse generically-depends-on specifically-depends-on continuant-part-of proper-continuant-part-of instance-of temporal-part-of has-member-part member-part-of)

  (cl:comment "member-part-of and has-member-part are inverse relations [jrm-1]"
    (forall (t a b) (iff (member-part-of a b t) (has-member-part b a t))))


  (cl:comment "member-part-of is dissective on third argument, a temporal region [yip-1]"
    (forall (p q r s)
     (if (and (member-part-of p q r) (temporal-part-of s r))
      (member-part-of p q s))))


  (cl:comment "An object aggregate always has at least one member [uhs-1]"
    (forall (ag t)
     (if (instance-of ag object-aggregate t)
      (exists (o1)
       (and (instance-of o1 object t) (member-part-of o1 ag t))))))


  (cl:comment "member-part-of is time indexed and has domain: object and range: object-aggregate [dvq-1]"
    (forall (a b t)
     (if (member-part-of a b t)
      (and (instance-of a object t) (instance-of b object-aggregate t)
       (instance-of t temporal-region t)))))


  (cl:comment "A fiat object part =def a proper part of an object [yir-1]"
    (forall (f t)
     (iff (instance-of f fiat-object-part t)
      (exists (o)
       (and (instance-of o object t) (proper-continuant-part-of f o t)
        (not (instance-of f immaterial-entity t)))))))


  (cl:comment "i is an immaterial entity = Def. i is an independent continuant that has no material entities as parts. [udu-1]"
    (forall (i t)
     (iff (instance-of i immaterial-entity t)
      (and (instance-of i independent-continuant t)
       (not
        (exists (m)
         (and (instance-of m material-entity t)
          (continuant-part-of m i t))))))))


  (cl:comment "Any continuant that doesn't s-depend or g-depend on something is an independant continuant [ilw-1]"
    (forall (c1)
     (iff (exists (t) (instance-of c1 independent-continuant t))
      (and (exists (t) (instance-of c1 continuant t))
       (not
        (exists (c2 t)
         (or (specifically-depends-on c1 c2)
          (generically-depends-on c1 c2 t))))))))


  (cl:comment "An object aggregate has more than one member at at least one time [ibd-1]"
    (forall (ag)
     (if (exists (t) (instance-of ag object-aggregate t))
      (exists (o1 o2 t)
       (and (not (= o1 o2)) (instance-of o1 object t)
        (member-part-of o1 ag t) (instance-of o2 object t)
        (member-part-of o2 ag t))))))


  (cl:comment "all parts of an aggregate overlap some member [fsy-1]"
    (forall (t b x)
     (if
      (and (proper-continuant-part-of x b t)
       (instance-of b object-aggregate t))
      (exists (o)
       (and (member-part-of o b t)
        (exists (z)
         (and (continuant-part-of z x t) (continuant-part-of z o t))))))))


  (cl:comment "If a material entity has a proper part, then at least one of its proper parts is not an immaterial entity [adm-1]"
    (forall (m t)
     (if
      (and (instance-of m material-entity t)
       (exists (mp) (and (continuant-part-of mp m t) (not (= mp m)))))
      (exists (mp)
       (and (not (= mp m)) (continuant-part-of mp m t)
        (not (instance-of mp immaterial-entity t)))))))


  (cl:comment "An object aggregate has member parts only disjoint objects [evk-1]"
    (forall (b c t)
     (iff (member-part-of b c t)
      (and (instance-of b object t) (instance-of c object-aggregate t)
       (proper-continuant-part-of b c t)
       (forall (d)
        (if (member-part-of d c t)
         (or (= b d)
          (not
           (exists (z)
            (and (continuant-part-of z b t)
             (continuant-part-of z d t)))))))))))

)))(cl:comment '
BFO 2020 Axiomatization, generated 2024/01/08
The most current version of this file will always be at the GitHub repository https://github.com/bfo-ontology/bfo-2020
Author: Alan Ruttenberg - alanruttenberg(at)gmail.com
This work is licensed under a Creative Commons "Attribution 4.0 International" license: https://creativecommons.org/licenses/by/4.0/'

 (cl:text

  (cl:ttl https://basic-formal-ontology.org/2020/formulas/clif/universal-declaration.cl

   (cl:outdiscourse exists-at entity temporal-part-of instance-of particular universal)

  (cl:comment "role is a universal [ewm-1]"
    (universal role))


  (cl:comment "site is a universal [yhb-1]"
    (universal site))


  (cl:comment "object is a universal [kxo-1]"
    (universal object))


  (cl:comment "history is a universal [gki-1]"
    (universal history))


  (cl:comment "process is a universal [bsm-1]"
    (universal process))


  (cl:comment "quality is a universal [mit-1]"
    (universal quality))


  (cl:comment "function is a universal [rym-1]"
    (universal function))


  (cl:comment "fiat-line is a universal [spk-1]"
    (universal fiat-line))


  (cl:comment "occurrent is a universal [lkt-1]"
    (universal occurrent))


  (cl:comment "continuant is a universal [axs-1]"
    (universal continuant))


  (cl:comment "fiat-point is a universal [rns-1]"
    (universal fiat-point))


  (cl:comment "disposition is a universal [mld-1]"
    (universal disposition))


  (cl:comment "fiat-surface is a universal [ebw-1]"
    (universal fiat-surface))


  (cl:comment "spatial-region is a universal [rej-1]"
    (universal spatial-region))


  (cl:comment "material-entity is a universal [hru-1]"
    (universal material-entity))


  (cl:comment "temporal-region is a universal [toj-1]"
    (universal temporal-region))


  (cl:comment "fiat-object-part is a universal [csp-1]"
    (universal fiat-object-part))


  (cl:comment "object-aggregate is a universal [cqv-1]"
    (universal object-aggregate))


  (cl:comment "process-boundary is a universal [zqv-1]"
    (universal process-boundary))


  (cl:comment "temporal-instant is a universal [bjs-1]"
    (universal temporal-instant))


  (cl:comment "immaterial-entity is a universal [zcc-1]"
    (universal immaterial-entity))


  (cl:comment "realizable-entity is a universal [gpp-1]"
    (universal realizable-entity))


  (cl:comment "temporal-interval is a universal [kuz-1]"
    (universal temporal-interval))


  (cl:comment "relational-quality is a universal [zrp-1]"
    (universal relational-quality))


  (cl:comment "spatiotemporal-region is a universal [mdh-1]"
    (universal spatiotemporal-region))


  (cl:comment "independent-continuant is a universal [ufw-1]"
    (universal independent-continuant))


  (cl:comment "continuant-fiat-boundary is a universal [zvi-1]"
    (universal continuant-fiat-boundary))


  (cl:comment "one-dimensional-spatial-region is a universal [zwl-1]"
    (universal one-dimensional-spatial-region))


  (cl:comment "two-dimensional-spatial-region is a universal [whi-1]"
    (universal two-dimensional-spatial-region))


  (cl:comment "one-dimensional-temporal-region is a universal [qar-1]"
    (universal one-dimensional-temporal-region))


  (cl:comment "zero-dimensional-spatial-region is a universal [vij-1]"
    (universal zero-dimensional-spatial-region))


  (cl:comment "generically-dependent-continuant is a universal [qiz-1]"
    (universal generically-dependent-continuant))


  (cl:comment "three-dimensional-spatial-region is a universal [qov-1]"
    (universal three-dimensional-spatial-region))


  (cl:comment "zero-dimensional-temporal-region is a universal [bau-1]"
    (universal zero-dimensional-temporal-region))


  (cl:comment "specifically-dependent-continuant is a universal [wda-1]"
    (universal specifically-dependent-continuant))


  (cl:comment "universals are not particulars [qkp-1]"
    (not (exists (x) (and (universal x) (particular x)))))


  (cl:comment "history is subclass of process [zuj-1]"
    (forall (t x)
     (if (instance-of x history t) (instance-of x process t))))


  (cl:comment "process is subclass of occurrent [lso-1]"
    (forall (t x)
     (if (instance-of x process t) (instance-of x occurrent t))))


  (cl:comment "function is subclass of disposition [lnj-1]"
    (forall (t x)
     (if (instance-of x function t) (instance-of x disposition t))))


  (cl:comment "object is subclass of material-entity [vbm-1]"
    (forall (t x)
     (if (instance-of x object t) (instance-of x material-entity t))))


  (cl:comment "role is subclass of realizable-entity [tcp-1]"
    (forall (t x)
     (if (instance-of x role t) (instance-of x realizable-entity t))))


  (cl:comment "site is subclass of immaterial-entity [tcd-1]"
    (forall (t x)
     (if (instance-of x site t) (instance-of x immaterial-entity t))))


  (cl:comment "If something is an instance of temporal region at t, then t is part of that temporal region [njq-1]"
    (forall (ti t)
     (if (instance-of ti temporal-region t) (temporal-part-of t ti))))


  (cl:comment "temporal-region is subclass of occurrent [ejl-1]"
    (forall (t x)
     (if (instance-of x temporal-region t) (instance-of x occurrent t))))


  (cl:comment "disposition, role are mutually disjoint [bwk-1]"
    (and
     (not
      (exists (x t)
       (and (instance-of x disposition t) (instance-of x role t))))))


  (cl:comment "process-boundary is subclass of occurrent [xot-1]"
    (forall (t x)
     (if (instance-of x process-boundary t) (instance-of x occurrent t))))


  (cl:comment "relational-quality is subclass of quality [taj-1]"
    (forall (t x)
     (if (instance-of x relational-quality t) (instance-of x quality t))))


  (cl:comment "disposition is subclass of realizable-entity [fxd-1]"
    (forall (t x)
     (if (instance-of x disposition t)
      (instance-of x realizable-entity t))))


  (cl:comment "continuant, occurrent are mutually disjoint [wrf-1]"
    (and
     (not
      (exists (x t)
       (and (instance-of x continuant t) (instance-of x occurrent t))))))


  (cl:comment "spatiotemporal-region is subclass of occurrent [les-1]"
    (forall (t x)
     (if (instance-of x spatiotemporal-region t)
      (instance-of x occurrent t))))


  (cl:comment "fiat-object-part is subclass of material-entity [lal-1]"
    (forall (t x)
     (if (instance-of x fiat-object-part t)
      (instance-of x material-entity t))))


  (cl:comment "object-aggregate is subclass of material-entity [fda-1]"
    (forall (t x)
     (if (instance-of x object-aggregate t)
      (instance-of x material-entity t))))


  (cl:comment "spatial-region is subclass of immaterial-entity [bre-1]"
    (forall (t x)
     (if (instance-of x spatial-region t)
      (instance-of x immaterial-entity t))))


  (cl:comment "independent-continuant is subclass of continuant [wyq-1]"
    (forall (t x)
     (if (instance-of x independent-continuant t)
      (instance-of x continuant t))))


  (cl:comment "fiat-line is subclass of continuant-fiat-boundary [dhy-1]"
    (forall (t x)
     (if (instance-of x fiat-line t)
      (instance-of x continuant-fiat-boundary t))))


  (cl:comment "quality, realizable-entity are mutually disjoint [ksk-1]"
    (and
     (not
      (exists (x t)
       (and (instance-of x quality t)
        (instance-of x realizable-entity t))))))


  (cl:comment "fiat-point is subclass of continuant-fiat-boundary [xlm-1]"
    (forall (t x)
     (if (instance-of x fiat-point t)
      (instance-of x continuant-fiat-boundary t))))


  (cl:comment "fiat-surface is subclass of continuant-fiat-boundary [kfj-1]"
    (forall (t x)
     (if (instance-of x fiat-surface t)
      (instance-of x continuant-fiat-boundary t))))


  (cl:comment "material-entity is subclass of independent-continuant [faf-1]"
    (forall (t x)
     (if (instance-of x material-entity t)
      (instance-of x independent-continuant t))))


  (cl:comment "immaterial-entity is subclass of independent-continuant [bzp-1]"
    (forall (t x)
     (if (instance-of x immaterial-entity t)
      (instance-of x independent-continuant t))))


  (cl:comment "quality is subclass of specifically-dependent-continuant [nbm-1]"
    (forall (t x)
     (if (instance-of x quality t)
      (instance-of x specifically-dependent-continuant t))))


  (cl:comment "continuant-fiat-boundary is subclass of immaterial-entity [tgs-1]"
    (forall (t x)
     (if (instance-of x continuant-fiat-boundary t)
      (instance-of x immaterial-entity t))))


  (cl:comment "material-entity, immaterial-entity are mutually disjoint [sij-1]"
    (and
     (not
      (exists (x t)
       (and (instance-of x material-entity t)
        (instance-of x immaterial-entity t))))))


  (cl:comment "generically-dependent-continuant is subclass of continuant [zyw-1]"
    (forall (t x)
     (if (instance-of x generically-dependent-continuant t)
      (instance-of x continuant t))))


  (cl:comment "specifically-dependent-continuant is subclass of continuant [dhv-1]"
    (forall (t x)
     (if (instance-of x specifically-dependent-continuant t)
      (instance-of x continuant t))))


  (cl:comment "one-dimensional-spatial-region is subclass of spatial-region [fzn-1]"
    (forall (t x)
     (if (instance-of x one-dimensional-spatial-region t)
      (instance-of x spatial-region t))))


  (cl:comment "two-dimensional-spatial-region is subclass of spatial-region [abo-1]"
    (forall (t x)
     (if (instance-of x two-dimensional-spatial-region t)
      (instance-of x spatial-region t))))


  (cl:comment "zero-dimensional-spatial-region is subclass of spatial-region [abh-1]"
    (forall (t x)
     (if (instance-of x zero-dimensional-spatial-region t)
      (instance-of x spatial-region t))))


  (cl:comment "one-dimensional-temporal-region is subclass of temporal-region [fpd-1]"
    (forall (t x)
     (if (instance-of x one-dimensional-temporal-region t)
      (instance-of x temporal-region t))))


  (cl:comment "three-dimensional-spatial-region is subclass of spatial-region [apt-1]"
    (forall (t x)
     (if (instance-of x three-dimensional-spatial-region t)
      (instance-of x spatial-region t))))


  (cl:comment "zero-dimensional-temporal-region is subclass of temporal-region [pvu-1]"
    (forall (t x)
     (if (instance-of x zero-dimensional-temporal-region t)
      (instance-of x temporal-region t))))


  (cl:comment "temporal-instant is subclass of zero-dimensional-temporal-region [bjp-1]"
    (forall (t x)
     (if (instance-of x temporal-instant t)
      (instance-of x zero-dimensional-temporal-region t))))


  (cl:comment "temporal-interval is subclass of one-dimensional-temporal-region [fye-1]"
    (forall (t x)
     (if (instance-of x temporal-interval t)
      (instance-of x one-dimensional-temporal-region t))))


  (cl:comment "Entity is either universal or particular, so not all are instantiated. Instead make a predicate 'entity' analogous to particular universal [vgn-1]"
    (forall (x)
     (if
      (exists (t)
       (or (instance-of x continuant t) (instance-of x occurrent t)))
      (entity x))))


  (cl:comment "realizable-entity is subclass of specifically-dependent-continuant [qix-1]"
    (forall (t x)
     (if (instance-of x realizable-entity t)
      (instance-of x specifically-dependent-continuant t))))


  (cl:comment "If something is a role at any time then as long as it exists it is a role. [hxo-1]"
    (forall (x)
     (if (exists (t) (instance-of x role t))
      (forall (t) (if (exists-at x t) (instance-of x role t))))))


  (cl:comment "If something is a site at any time then as long as it exists it is a site. [txn-1]"
    (forall (x)
     (if (exists (t) (instance-of x site t))
      (forall (t) (if (exists-at x t) (instance-of x site t))))))


  (cl:comment "If something is a quality at any time then as long as it exists it is a quality. [jdo-1]"
    (forall (x)
     (if (exists (t) (instance-of x quality t))
      (forall (t) (if (exists-at x t) (instance-of x quality t))))))


  (cl:comment "If something is a function at any time then as long as it exists it is a function. [hww-1]"
    (forall (x)
     (if (exists (t) (instance-of x function t))
      (forall (t) (if (exists-at x t) (instance-of x function t))))))


  (cl:comment "one-dimensional-temporal-region, zero-dimensional-temporal-region are mutually disjoint [zkj-1]"
    (and
     (not
      (exists (x t)
       (and (instance-of x one-dimensional-temporal-region t)
        (instance-of x zero-dimensional-temporal-region t))))))


  (cl:comment "If something is a fiat-line at any time then as long as it exists it is a fiat-line. [ylr-1]"
    (forall (x)
     (if (exists (t) (instance-of x fiat-line t))
      (forall (t) (if (exists-at x t) (instance-of x fiat-line t))))))


  (cl:comment "If something is a continuant at any time then as long as it exists it is a continuant. [ghs-1]"
    (forall (x)
     (if (exists (t) (instance-of x continuant t))
      (forall (t) (if (exists-at x t) (instance-of x continuant t))))))


  (cl:comment "If something is a fiat-point at any time then as long as it exists it is a fiat-point. [cqf-1]"
    (forall (x)
     (if (exists (t) (instance-of x fiat-point t))
      (forall (t) (if (exists-at x t) (instance-of x fiat-point t))))))


  (cl:comment "If something is a disposition at any time then as long as it exists it is a disposition. [ijx-1]"
    (forall (x)
     (if (exists (t) (instance-of x disposition t))
      (forall (t) (if (exists-at x t) (instance-of x disposition t))))))


  (cl:comment "If something is a fiat-surface at any time then as long as it exists it is a fiat-surface. [dyv-1]"
    (forall (x)
     (if (exists (t) (instance-of x fiat-surface t))
      (forall (t) (if (exists-at x t) (instance-of x fiat-surface t))))))


  (cl:comment "If something is a spatial-region at any time then as long as it exists it is a spatial-region. [thk-1]"
    (forall (x)
     (if (exists (t) (instance-of x spatial-region t))
      (forall (t) (if (exists-at x t) (instance-of x spatial-region t))))))


  (cl:comment "If something is a material-entity at any time then as long as it exists it is a material-entity. [opd-1]"
    (forall (x)
     (if (exists (t) (instance-of x material-entity t))
      (forall (t)
       (if (exists-at x t) (instance-of x material-entity t))))))


  (cl:comment "If something is a immaterial-entity at any time then as long as it exists it is a immaterial-entity. [nlc-1]"
    (forall (x)
     (if (exists (t) (instance-of x immaterial-entity t))
      (forall (t)
       (if (exists-at x t) (instance-of x immaterial-entity t))))))


  (cl:comment "If something is a realizable-entity at any time then as long as it exists it is a realizable-entity. [gsg-1]"
    (forall (x)
     (if (exists (t) (instance-of x realizable-entity t))
      (forall (t)
       (if (exists-at x t) (instance-of x realizable-entity t))))))


  (cl:comment "If something is a relational-quality at any time then as long as it exists it is a relational-quality. [jyh-1]"
    (forall (x)
     (if (exists (t) (instance-of x relational-quality t))
      (forall (t)
       (if (exists-at x t) (instance-of x relational-quality t))))))


  (cl:comment "If something is a independent-continuant at any time then as long as it exists it is a independent-continuant. [otk-1]"
    (forall (x)
     (if (exists (t) (instance-of x independent-continuant t))
      (forall (t)
       (if (exists-at x t) (instance-of x independent-continuant t))))))


  (cl:comment "If something is a continuant-fiat-boundary at any time then as long as it exists it is a continuant-fiat-boundary. [yuh-1]"
    (forall (x)
     (if (exists (t) (instance-of x continuant-fiat-boundary t))
      (forall (t)
       (if (exists-at x t) (instance-of x continuant-fiat-boundary t))))))


  (cl:comment "If something is a one-dimensional-spatial-region at any time then as long as it exists it is a one-dimensional-spatial-region. [bld-1]"
    (forall (x)
     (if (exists (t) (instance-of x one-dimensional-spatial-region t))
      (forall (t)
       (if (exists-at x t)
        (instance-of x one-dimensional-spatial-region t))))))


  (cl:comment "If something is a two-dimensional-spatial-region at any time then as long as it exists it is a two-dimensional-spatial-region. [uld-1]"
    (forall (x)
     (if (exists (t) (instance-of x two-dimensional-spatial-region t))
      (forall (t)
       (if (exists-at x t)
        (instance-of x two-dimensional-spatial-region t))))))


  (cl:comment "If something is a zero-dimensional-spatial-region at any time then as long as it exists it is a zero-dimensional-spatial-region. [vsa-1]"
    (forall (x)
     (if (exists (t) (instance-of x zero-dimensional-spatial-region t))
      (forall (t)
       (if (exists-at x t)
        (instance-of x zero-dimensional-spatial-region t))))))


  (cl:comment "If something is a generically-dependent-continuant at any time then as long as it exists it is a generically-dependent-continuant. [iup-1]"
    (forall (x)
     (if (exists (t) (instance-of x generically-dependent-continuant t))
      (forall (t)
       (if (exists-at x t)
        (instance-of x generically-dependent-continuant t))))))


  (cl:comment "If something is a three-dimensional-spatial-region at any time then as long as it exists it is a three-dimensional-spatial-region. [qpr-1]"
    (forall (x)
     (if (exists (t) (instance-of x three-dimensional-spatial-region t))
      (forall (t)
       (if (exists-at x t)
        (instance-of x three-dimensional-spatial-region t))))))


  (cl:comment "If something is a specifically-dependent-continuant at any time then as long as it exists it is a specifically-dependent-continuant. [hke-1]"
    (forall (x)
     (if (exists (t) (instance-of x specifically-dependent-continuant t))
      (forall (t)
       (if (exists-at x t)
        (instance-of x specifically-dependent-continuant t))))))


  (cl:comment "No occurrent changes type during its existence [ayr-1]"
    (forall (o)
     (if (exists (t) (instance-of o occurrent t))
      (forall (u)
       (if (exists (t) (instance-of o u t))
        (forall (t)
         (iff (instance-of o occurrent t) (instance-of o u t))))))))


  (cl:comment "fiat-surface, fiat-line, fiat-point are mutually disjoint [sjf-1]"
    (and
     (not
      (exists (x t)
       (and (instance-of x fiat-surface t) (instance-of x fiat-line t))))
     (not
      (exists (x t)
       (and (instance-of x fiat-surface t)
        (instance-of x fiat-point t))))
     (not
      (exists (x t)
       (and (instance-of x fiat-line t) (instance-of x fiat-point t))))))


  (cl:comment "site, spatial-region, continuant-fiat-boundary are mutually disjoint [twc-1]"
    (and
     (not
      (exists (x t)
       (and (instance-of x site t) (instance-of x spatial-region t))))
     (not
      (exists (x t)
       (and (instance-of x site t)
        (instance-of x continuant-fiat-boundary t))))
     (not
      (exists (x t)
       (and (instance-of x spatial-region t)
        (instance-of x continuant-fiat-boundary t))))))


  (cl:comment "specifically-dependent-continuant, independent-continuant, generically-dependent-continuant are mutually disjoint [cig-1]"
    (and
     (not
      (exists (x t)
       (and (instance-of x specifically-dependent-continuant t)
        (instance-of x independent-continuant t))))
     (not
      (exists (x t)
       (and (instance-of x specifically-dependent-continuant t)
        (instance-of x generically-dependent-continuant t))))
     (not
      (exists (x t)
       (and (instance-of x independent-continuant t)
        (instance-of x generically-dependent-continuant t))))))


  (cl:comment "process, spatiotemporal-region, process-boundary, temporal-region are mutually disjoint [mem-1]"
    (and
     (not
      (exists (x t)
       (and (instance-of x process t)
        (instance-of x spatiotemporal-region t))))
     (not
      (exists (x t)
       (and (instance-of x process t)
        (instance-of x process-boundary t))))
     (not
      (exists (x t)
       (and (instance-of x process t)
        (instance-of x temporal-region t))))
     (not
      (exists (x t)
       (and (instance-of x spatiotemporal-region t)
        (instance-of x process-boundary t))))
     (not
      (exists (x t)
       (and (instance-of x spatiotemporal-region t)
        (instance-of x temporal-region t))))
     (not
      (exists (x t)
       (and (instance-of x process-boundary t)
        (instance-of x temporal-region t))))))


  (cl:comment "continuant, material-entity, object, fiat-object-part, object-aggregate, site, immaterial-entity, continuant-fiat-boundary, fiat-surface, fiat-line, fiat-point, spatial-region, three-dimensional-spatial-region, two-dimensional-spatial-region, one-dimensional-spatial-region, zero-dimensional-spatial-region, independent-continuant, generically-dependent-continuant, specifically-dependent-continuant, quality, relational-quality, function, disposition, realizable-entity, role, occurrent, process, process-boundary, temporal-region, zero-dimensional-temporal-region, temporal-instant, one-dimensional-temporal-region, temporal-interval, history, spatiotemporal-region are all different [xtf-1]"
    (and (not (= continuant material-entity))
         (not (= continuant object))
         (not (= continuant fiat-object-part))
         (not (= continuant object-aggregate))
         (not (= continuant site))
         (not (= continuant immaterial-entity))
         (not (= continuant continuant-fiat-boundary))
         (not (= continuant fiat-surface))
         (not (= continuant fiat-line))
         (not (= continuant fiat-point))
         (not (= continuant spatial-region))
         (not (= continuant three-dimensional-spatial-region))
         (not (= continuant two-dimensional-spatial-region))
         (not (= continuant one-dimensional-spatial-region))
         (not (= continuant zero-dimensional-spatial-region))
         (not (= continuant independent-continuant))
         (not (= continuant generically-dependent-continuant))
         (not (= continuant specifically-dependent-continuant))
         (not (= continuant quality))
         (not (= continuant relational-quality))
         (not (= continuant function))
         (not (= continuant disposition))
         (not (= continuant realizable-entity))
         (not (= continuant role))
         (not (= continuant occurrent))
         (not (= continuant process))
         (not (= continuant process-boundary))
         (not (= continuant temporal-region))
         (not (= continuant zero-dimensional-temporal-region))
         (not (= continuant temporal-instant))
         (not (= continuant one-dimensional-temporal-region))
         (not (= continuant temporal-interval))
         (not (= continuant history))
         (not (= continuant spatiotemporal-region))
         (not (= material-entity object))
         (not (= material-entity fiat-object-part))
         (not (= material-entity object-aggregate))
         (not (= material-entity site))
         (not (= material-entity immaterial-entity))
         (not (= material-entity continuant-fiat-boundary))
         (not (= material-entity fiat-surface))
         (not (= material-entity fiat-line))
         (not (= material-entity fiat-point))
         (not (= material-entity spatial-region))
         (not (= material-entity three-dimensional-spatial-region))
         (not (= material-entity two-dimensional-spatial-region))
         (not (= material-entity one-dimensional-spatial-region))
         (not (= material-entity zero-dimensional-spatial-region))
         (not (= material-entity independent-continuant))
         (not (= material-entity generically-dependent-continuant))
         (not (= material-entity specifically-dependent-continuant))
         (not (= material-entity quality))
         (not (= material-entity relational-quality))
         (not (= material-entity function))
         (not (= material-entity disposition))
         (not (= material-entity realizable-entity))
         (not (= material-entity role))
         (not (= material-entity occurrent))
         (not (= material-entity process))
         (not (= material-entity process-boundary))
         (not (= material-entity temporal-region))
         (not (= material-entity zero-dimensional-temporal-region))
         (not (= material-entity temporal-instant))
         (not (= material-entity one-dimensional-temporal-region))
         (not (= material-entity temporal-interval))
         (not (= material-entity history))
         (not (= material-entity spatiotemporal-region))
         (not (= object fiat-object-part))
         (not (= object object-aggregate))
         (not (= object site))
         (not (= object immaterial-entity))
         (not (= object continuant-fiat-boundary))
         (not (= object fiat-surface))
         (not (= object fiat-line))
         (not (= object fiat-point))
         (not (= object spatial-region))
         (not (= object three-dimensional-spatial-region))
         (not (= object two-dimensional-spatial-region))
         (not (= object one-dimensional-spatial-region))
         (not (= object zero-dimensional-spatial-region))
         (not (= object independent-continuant))
         (not (= object generically-dependent-continuant))
         (not (= object specifically-dependent-continuant))
         (not (= object quality))
         (not (= object relational-quality))
         (not (= object function))
         (not (= object disposition))
         (not (= object realizable-entity))
         (not (= object role))
         (not (= object occurrent))
         (not (= object process))
         (not (= object process-boundary))
         (not (= object temporal-region))
         (not (= object zero-dimensional-temporal-region))
         (not (= object temporal-instant))
         (not (= object one-dimensional-temporal-region))
         (not (= object temporal-interval))
         (not (= object history))
         (not (= object spatiotemporal-region))
         (not (= fiat-object-part object-aggregate))
         (not (= fiat-object-part site))
         (not (= fiat-object-part immaterial-entity))
         (not (= fiat-object-part continuant-fiat-boundary))
         (not (= fiat-object-part fiat-surface))
         (not (= fiat-object-part fiat-line))
         (not (= fiat-object-part fiat-point))
         (not (= fiat-object-part spatial-region))
         (not (= fiat-object-part three-dimensional-spatial-region))
         (not (= fiat-object-part two-dimensional-spatial-region))
         (not (= fiat-object-part one-dimensional-spatial-region))
         (not (= fiat-object-part zero-dimensional-spatial-region))
         (not (= fiat-object-part independent-continuant))
         (not (= fiat-object-part generically-dependent-continuant))
         (not (= fiat-object-part specifically-dependent-continuant))
         (not (= fiat-object-part quality))
         (not (= fiat-object-part relational-quality))
         (not (= fiat-object-part function))
         (not (= fiat-object-part disposition))
         (not (= fiat-object-part realizable-entity))
         (not (= fiat-object-part role))
         (not (= fiat-object-part occurrent))
         (not (= fiat-object-part process))
         (not (= fiat-object-part process-boundary))
         (not (= fiat-object-part temporal-region))
         (not (= fiat-object-part zero-dimensional-temporal-region))
         (not (= fiat-object-part temporal-instant))
         (not (= fiat-object-part one-dimensional-temporal-region))
         (not (= fiat-object-part temporal-interval))
         (not (= fiat-object-part history))
         (not (= fiat-object-part spatiotemporal-region))
         (not (= object-aggregate site))
         (not (= object-aggregate immaterial-entity))
         (not (= object-aggregate continuant-fiat-boundary))
         (not (= object-aggregate fiat-surface))
         (not (= object-aggregate fiat-line))
         (not (= object-aggregate fiat-point))
         (not (= object-aggregate spatial-region))
         (not (= object-aggregate three-dimensional-spatial-region))
         (not (= object-aggregate two-dimensional-spatial-region))
         (not (= object-aggregate one-dimensional-spatial-region))
         (not (= object-aggregate zero-dimensional-spatial-region))
         (not (= object-aggregate independent-continuant))
         (not (= object-aggregate generically-dependent-continuant))
         (not (= object-aggregate specifically-dependent-continuant))
         (not (= object-aggregate quality))
         (not (= object-aggregate relational-quality))
         (not (= object-aggregate function))
         (not (= object-aggregate disposition))
         (not (= object-aggregate realizable-entity))
         (not (= object-aggregate role))
         (not (= object-aggregate occurrent))
         (not (= object-aggregate process))
         (not (= object-aggregate process-boundary))
         (not (= object-aggregate temporal-region))
         (not (= object-aggregate zero-dimensional-temporal-region))
         (not (= object-aggregate temporal-instant))
         (not (= object-aggregate one-dimensional-temporal-region))
         (not (= object-aggregate temporal-interval))
         (not (= object-aggregate history))
         (not (= object-aggregate spatiotemporal-region))
         (not (= site immaterial-entity))
         (not (= site continuant-fiat-boundary))
         (not (= site fiat-surface))
         (not (= site fiat-line))
         (not (= site fiat-point))
         (not (= site spatial-region))
         (not (= site three-dimensional-spatial-region))
         (not (= site two-dimensional-spatial-region))
         (not (= site one-dimensional-spatial-region))
         (not (= site zero-dimensional-spatial-region))
         (not (= site independent-continuant))
         (not (= site generically-dependent-continuant))
         (not (= site specifically-dependent-continuant))
         (not (= site quality))
         (not (= site relational-quality))
         (not (= site function))
         (not (= site disposition))
         (not (= site realizable-entity))
         (not (= site role))
         (not (= site occurrent))
         (not (= site process))
         (not (= site process-boundary))
         (not (= site temporal-region))
         (not (= site zero-dimensional-temporal-region))
         (not (= site temporal-instant))
         (not (= site one-dimensional-temporal-region))
         (not (= site temporal-interval))
         (not (= site history))
         (not (= site spatiotemporal-region))
         (not (= immaterial-entity continuant-fiat-boundary))
         (not (= immaterial-entity fiat-surface))
         (not (= immaterial-entity fiat-line))
         (not (= immaterial-entity fiat-point))
         (not (= immaterial-entity spatial-region))
         (not (= immaterial-entity three-dimensional-spatial-region))
         (not (= immaterial-entity two-dimensional-spatial-region))
         (not (= immaterial-entity one-dimensional-spatial-region))
         (not (= immaterial-entity zero-dimensional-spatial-region))
         (not (= immaterial-entity independent-continuant))
         (not (= immaterial-entity generically-dependent-continuant))
         (not (= immaterial-entity specifically-dependent-continuant))
         (not (= immaterial-entity quality))
         (not (= immaterial-entity relational-quality))
         (not (= immaterial-entity function))
         (not (= immaterial-entity disposition))
         (not (= immaterial-entity realizable-entity))
         (not (= immaterial-entity role))
         (not (= immaterial-entity occurrent))
         (not (= immaterial-entity process))
         (not (= immaterial-entity process-boundary))
         (not (= immaterial-entity temporal-region))
         (not (= immaterial-entity zero-dimensional-temporal-region))
         (not (= immaterial-entity temporal-instant))
         (not (= immaterial-entity one-dimensional-temporal-region))
         (not (= immaterial-entity temporal-interval))
         (not (= immaterial-entity history))
         (not (= immaterial-entity spatiotemporal-region))
         (not (= continuant-fiat-boundary fiat-surface))
         (not (= continuant-fiat-boundary fiat-line))
         (not (= continuant-fiat-boundary fiat-point))
         (not (= continuant-fiat-boundary spatial-region))
         (not (= continuant-fiat-boundary
                 three-dimensional-spatial-region))
         (not (= continuant-fiat-boundary
                 two-dimensional-spatial-region))
         (not (= continuant-fiat-boundary
                 one-dimensional-spatial-region))
         (not (= continuant-fiat-boundary
                 zero-dimensional-spatial-region))
         (not (= continuant-fiat-boundary independent-continuant))
         (not (= continuant-fiat-boundary
                 generically-dependent-continuant))
         (not (= continuant-fiat-boundary
                 specifically-dependent-continuant))
         (not (= continuant-fiat-boundary quality))
         (not (= continuant-fiat-boundary relational-quality))
         (not (= continuant-fiat-boundary function))
         (not (= continuant-fiat-boundary disposition))
         (not (= continuant-fiat-boundary realizable-entity))
         (not (= continuant-fiat-boundary role))
         (not (= continuant-fiat-boundary occurrent))
         (not (= continuant-fiat-boundary process))
         (not (= continuant-fiat-boundary process-boundary))
         (not (= continuant-fiat-boundary temporal-region))
         (not (= continuant-fiat-boundary
                 zero-dimensional-temporal-region))
         (not (= continuant-fiat-boundary temporal-instant))
         (not (= continuant-fiat-boundary
                 one-dimensional-temporal-region))
         (not (= continuant-fiat-boundary temporal-interval))
         (not (= continuant-fiat-boundary history))
         (not (= continuant-fiat-boundary spatiotemporal-region))
         (not (= fiat-surface fiat-line))
         (not (= fiat-surface fiat-point))
         (not (= fiat-surface spatial-region))
         (not (= fiat-surface three-dimensional-spatial-region))
         (not (= fiat-surface two-dimensional-spatial-region))
         (not (= fiat-surface one-dimensional-spatial-region))
         (not (= fiat-surface zero-dimensional-spatial-region))
         (not (= fiat-surface independent-continuant))
         (not (= fiat-surface generically-dependent-continuant))
         (not (= fiat-surface specifically-dependent-continuant))
         (not (= fiat-surface quality))
         (not (= fiat-surface relational-quality))
         (not (= fiat-surface function))
         (not (= fiat-surface disposition))
         (not (= fiat-surface realizable-entity))
         (not (= fiat-surface role))
         (not (= fiat-surface occurrent))
         (not (= fiat-surface process))
         (not (= fiat-surface process-boundary))
         (not (= fiat-surface temporal-region))
         (not (= fiat-surface zero-dimensional-temporal-region))
         (not (= fiat-surface temporal-instant))
         (not (= fiat-surface one-dimensional-temporal-region))
         (not (= fiat-surface temporal-interval))
         (not (= fiat-surface history))
         (not (= fiat-surface spatiotemporal-region))
         (not (= fiat-line fiat-point))
         (not (= fiat-line spatial-region))
         (not (= fiat-line three-dimensional-spatial-region))
         (not (= fiat-line two-dimensional-spatial-region))
         (not (= fiat-line one-dimensional-spatial-region))
         (not (= fiat-line zero-dimensional-spatial-region))
         (not (= fiat-line independent-continuant))
         (not (= fiat-line generically-dependent-continuant))
         (not (= fiat-line specifically-dependent-continuant))
         (not (= fiat-line quality))
         (not (= fiat-line relational-quality))
         (not (= fiat-line function))
         (not (= fiat-line disposition))
         (not (= fiat-line realizable-entity))
         (not (= fiat-line role))
         (not (= fiat-line occurrent))
         (not (= fiat-line process))
         (not (= fiat-line process-boundary))
         (not (= fiat-line temporal-region))
         (not (= fiat-line zero-dimensional-temporal-region))
         (not (= fiat-line temporal-instant))
         (not (= fiat-line one-dimensional-temporal-region))
         (not (= fiat-line temporal-interval))
         (not (= fiat-line history))
         (not (= fiat-line spatiotemporal-region))
         (not (= fiat-point spatial-region))
         (not (= fiat-point three-dimensional-spatial-region))
         (not (= fiat-point two-dimensional-spatial-region))
         (not (= fiat-point one-dimensional-spatial-region))
         (not (= fiat-point zero-dimensional-spatial-region))
         (not (= fiat-point independent-continuant))
         (not (= fiat-point generically-dependent-continuant))
         (not (= fiat-point specifically-dependent-continuant))
         (not (= fiat-point quality))
         (not (= fiat-point relational-quality))
         (not (= fiat-point function))
         (not (= fiat-point disposition))
         (not (= fiat-point realizable-entity))
         (not (= fiat-point role))
         (not (= fiat-point occurrent))
         (not (= fiat-point process))
         (not (= fiat-point process-boundary))
         (not (= fiat-point temporal-region))
         (not (= fiat-point zero-dimensional-temporal-region))
         (not (= fiat-point temporal-instant))
         (not (= fiat-point one-dimensional-temporal-region))
         (not (= fiat-point temporal-interval))
         (not (= fiat-point history))
         (not (= fiat-point spatiotemporal-region))
         (not (= spatial-region three-dimensional-spatial-region))
         (not (= spatial-region two-dimensional-spatial-region))
         (not (= spatial-region one-dimensional-spatial-region))
         (not (= spatial-region zero-dimensional-spatial-region))
         (not (= spatial-region independent-continuant))
         (not (= spatial-region generically-dependent-continuant))
         (not (= spatial-region specifically-dependent-continuant))
         (not (= spatial-region quality))
         (not (= spatial-region relational-quality))
         (not (= spatial-region function))
         (not (= spatial-region disposition))
         (not (= spatial-region realizable-entity))
         (not (= spatial-region role))
         (not (= spatial-region occurrent))
         (not (= spatial-region process))
         (not (= spatial-region process-boundary))
         (not (= spatial-region temporal-region))
         (not (= spatial-region zero-dimensional-temporal-region))
         (not (= spatial-region temporal-instant))
         (not (= spatial-region one-dimensional-temporal-region))
         (not (= spatial-region temporal-interval))
         (not (= spatial-region history))
         (not (= spatial-region spatiotemporal-region))
         (not (= three-dimensional-spatial-region
                 two-dimensional-spatial-region))
         (not (= three-dimensional-spatial-region
                 one-dimensional-spatial-region))
         (not (= three-dimensional-spatial-region
                 zero-dimensional-spatial-region))
         (not (= three-dimensional-spatial-region
                 independent-continuant))
         (not (= three-dimensional-spatial-region
                 generically-dependent-continuant))
         (not (= three-dimensional-spatial-region
                 specifically-dependent-continuant))
         (not (= three-dimensional-spatial-region quality))
         (not (= three-dimensional-spatial-region relational-quality))
         (not (= three-dimensional-spatial-region function))
         (not (= three-dimensional-spatial-region disposition))
         (not (= three-dimensional-spatial-region realizable-entity))
         (not (= three-dimensional-spatial-region role))
         (not (= three-dimensional-spatial-region occurrent))
         (not (= three-dimensional-spatial-region process))
         (not (= three-dimensional-spatial-region process-boundary))
         (not (= three-dimensional-spatial-region temporal-region))
         (not (= three-dimensional-spatial-region
                 zero-dimensional-temporal-region))
         (not (= three-dimensional-spatial-region temporal-instant))
         (not (= three-dimensional-spatial-region
                 one-dimensional-temporal-region))
         (not (= three-dimensional-spatial-region temporal-interval))
         (not (= three-dimensional-spatial-region history))
         (not (= three-dimensional-spatial-region spatiotemporal-region))
         (not (= two-dimensional-spatial-region
                 one-dimensional-spatial-region))
         (not (= two-dimensional-spatial-region
                 zero-dimensional-spatial-region))
         (not (= two-dimensional-spatial-region independent-continuant))
         (not (= two-dimensional-spatial-region
                 generically-dependent-continuant))
         (not (= two-dimensional-spatial-region
                 specifically-dependent-continuant))
         (not (= two-dimensional-spatial-region quality))
         (not (= two-dimensional-spatial-region relational-quality))
         (not (= two-dimensional-spatial-region function))
         (not (= two-dimensional-spatial-region disposition))
         (not (= two-dimensional-spatial-region realizable-entity))
         (not (= two-dimensional-spatial-region role))
         (not (= two-dimensional-spatial-region occurrent))
         (not (= two-dimensional-spatial-region process))
         (not (= two-dimensional-spatial-region process-boundary))
         (not (= two-dimensional-spatial-region temporal-region))
         (not (= two-dimensional-spatial-region
                 zero-dimensional-temporal-region))
         (not (= two-dimensional-spatial-region temporal-instant))
         (not (= two-dimensional-spatial-region
                 one-dimensional-temporal-region))
         (not (= two-dimensional-spatial-region temporal-interval))
         (not (= two-dimensional-spatial-region history))
         (not (= two-dimensional-spatial-region spatiotemporal-region))
         (not (= one-dimensional-spatial-region
                 zero-dimensional-spatial-region))
         (not (= one-dimensional-spatial-region independent-continuant))
         (not (= one-dimensional-spatial-region
                 generically-dependent-continuant))
         (not (= one-dimensional-spatial-region
                 specifically-dependent-continuant))
         (not (= one-dimensional-spatial-region quality))
         (not (= one-dimensional-spatial-region relational-quality))
         (not (= one-dimensional-spatial-region function))
         (not (= one-dimensional-spatial-region disposition))
         (not (= one-dimensional-spatial-region realizable-entity))
         (not (= one-dimensional-spatial-region role))
         (not (= one-dimensional-spatial-region occurrent))
         (not (= one-dimensional-spatial-region process))
         (not (= one-dimensional-spatial-region process-boundary))
         (not (= one-dimensional-spatial-region temporal-region))
         (not (= one-dimensional-spatial-region
                 zero-dimensional-temporal-region))
         (not (= one-dimensional-spatial-region temporal-instant))
         (not (= one-dimensional-spatial-region
                 one-dimensional-temporal-region))
         (not (= one-dimensional-spatial-region temporal-interval))
         (not (= one-dimensional-spatial-region history))
         (not (= one-dimensional-spatial-region spatiotemporal-region))
         (not (= zero-dimensional-spatial-region independent-continuant))
         (not (= zero-dimensional-spatial-region
                 generically-dependent-continuant))
         (not (= zero-dimensional-spatial-region
                 specifically-dependent-continuant))
         (not (= zero-dimensional-spatial-region quality))
         (not (= zero-dimensional-spatial-region relational-quality))
         (not (= zero-dimensional-spatial-region function))
         (not (= zero-dimensional-spatial-region disposition))
         (not (= zero-dimensional-spatial-region realizable-entity))
         (not (= zero-dimensional-spatial-region role))
         (not (= zero-dimensional-spatial-region occurrent))
         (not (= zero-dimensional-spatial-region process))
         (not (= zero-dimensional-spatial-region process-boundary))
         (not (= zero-dimensional-spatial-region temporal-region))
         (not (= zero-dimensional-spatial-region
                 zero-dimensional-temporal-region))
         (not (= zero-dimensional-spatial-region temporal-instant))
         (not (= zero-dimensional-spatial-region
                 one-dimensional-temporal-region))
         (not (= zero-dimensional-spatial-region temporal-interval))
         (not (= zero-dimensional-spatial-region history))
         (not (= zero-dimensional-spatial-region spatiotemporal-region))
         (not (= independent-continuant
                 generically-dependent-continuant))
         (not (= independent-continuant
                 specifically-dependent-continuant))
         (not (= independent-continuant quality))
         (not (= independent-continuant relational-quality))
         (not (= independent-continuant function))
         (not (= independent-continuant disposition))
         (not (= independent-continuant realizable-entity))
         (not (= independent-continuant role))
         (not (= independent-continuant occurrent))
         (not (= independent-continuant process))
         (not (= independent-continuant process-boundary))
         (not (= independent-continuant temporal-region))
         (not (= independent-continuant
                 zero-dimensional-temporal-region))
         (not (= independent-continuant temporal-instant))
         (not (= independent-continuant one-dimensional-temporal-region))
         (not (= independent-continuant temporal-interval))
         (not (= independent-continuant history))
         (not (= independent-continuant spatiotemporal-region))
         (not (= generically-dependent-continuant
                 specifically-dependent-continuant))
         (not (= generically-dependent-continuant quality))
         (not (= generically-dependent-continuant relational-quality))
         (not (= generically-dependent-continuant function))
         (not (= generically-dependent-continuant disposition))
         (not (= generically-dependent-continuant realizable-entity))
         (not (= generically-dependent-continuant role))
         (not (= generically-dependent-continuant occurrent))
         (not (= generically-dependent-continuant process))
         (not (= generically-dependent-continuant process-boundary))
         (not (= generically-dependent-continuant temporal-region))
         (not (= generically-dependent-continuant
                 zero-dimensional-temporal-region))
         (not (= generically-dependent-continuant temporal-instant))
         (not (= generically-dependent-continuant
                 one-dimensional-temporal-region))
         (not (= generically-dependent-continuant temporal-interval))
         (not (= generically-dependent-continuant history))
         (not (= generically-dependent-continuant spatiotemporal-region))
         (not (= specifically-dependent-continuant quality))
         (not (= specifically-dependent-continuant relational-quality))
         (not (= specifically-dependent-continuant function))
         (not (= specifically-dependent-continuant disposition))
         (not (= specifically-dependent-continuant realizable-entity))
         (not (= specifically-dependent-continuant role))
         (not (= specifically-dependent-continuant occurrent))
         (not (= specifically-dependent-continuant process))
         (not (= specifically-dependent-continuant process-boundary))
         (not (= specifically-dependent-continuant temporal-region))
         (not (= specifically-dependent-continuant
                 zero-dimensional-temporal-region))
         (not (= specifically-dependent-continuant temporal-instant))
         (not (= specifically-dependent-continuant
                 one-dimensional-temporal-region))
         (not (= specifically-dependent-continuant temporal-interval))
         (not (= specifically-dependent-continuant history))
         (not (= specifically-dependent-continuant
                 spatiotemporal-region))
         (not (= quality relational-quality))
         (not (= quality function))
         (not (= quality disposition))
         (not (= quality realizable-entity))
         (not (= quality role))
         (not (= quality occurrent))
         (not (= quality process))
         (not (= quality process-boundary))
         (not (= quality temporal-region))
         (not (= quality zero-dimensional-temporal-region))
         (not (= quality temporal-instant))
         (not (= quality one-dimensional-temporal-region))
         (not (= quality temporal-interval))
         (not (= quality history))
         (not (= quality spatiotemporal-region))
         (not (= relational-quality function))
         (not (= relational-quality disposition))
         (not (= relational-quality realizable-entity))
         (not (= relational-quality role))
         (not (= relational-quality occurrent))
         (not (= relational-quality process))
         (not (= relational-quality process-boundary))
         (not (= relational-quality temporal-region))
         (not (= relational-quality zero-dimensional-temporal-region))
         (not (= relational-quality temporal-instant))
         (not (= relational-quality one-dimensional-temporal-region))
         (not (= relational-quality temporal-interval))
         (not (= relational-quality history))
         (not (= relational-quality spatiotemporal-region))
         (not (= function disposition))
         (not (= function realizable-entity))
         (not (= function role))
         (not (= function occurrent))
         (not (= function process))
         (not (= function process-boundary))
         (not (= function temporal-region))
         (not (= function zero-dimensional-temporal-region))
         (not (= function temporal-instant))
         (not (= function one-dimensional-temporal-region))
         (not (= function temporal-interval))
         (not (= function history))
         (not (= function spatiotemporal-region))
         (not (= disposition realizable-entity))
         (not (= disposition role))
         (not (= disposition occurrent))
         (not (= disposition process))
         (not (= disposition process-boundary))
         (not (= disposition temporal-region))
         (not (= disposition zero-dimensional-temporal-region))
         (not (= disposition temporal-instant))
         (not (= disposition one-dimensional-temporal-region))
         (not (= disposition temporal-interval))
         (not (= disposition history))
         (not (= disposition spatiotemporal-region))
         (not (= realizable-entity role))
         (not (= realizable-entity occurrent))
         (not (= realizable-entity process))
         (not (= realizable-entity process-boundary))
         (not (= realizable-entity temporal-region))
         (not (= realizable-entity zero-dimensional-temporal-region))
         (not (= realizable-entity temporal-instant))
         (not (= realizable-entity one-dimensional-temporal-region))
         (not (= realizable-entity temporal-interval))
         (not (= realizable-entity history))
         (not (= realizable-entity spatiotemporal-region))
         (not (= role occurrent))
         (not (= role process))
         (not (= role process-boundary))
         (not (= role temporal-region))
         (not (= role zero-dimensional-temporal-region))
         (not (= role temporal-instant))
         (not (= role one-dimensional-temporal-region))
         (not (= role temporal-interval))
         (not (= role history))
         (not (= role spatiotemporal-region))
         (not (= occurrent process))
         (not (= occurrent process-boundary))
         (not (= occurrent temporal-region))
         (not (= occurrent zero-dimensional-temporal-region))
         (not (= occurrent temporal-instant))
         (not (= occurrent one-dimensional-temporal-region))
         (not (= occurrent temporal-interval))
         (not (= occurrent history))
         (not (= occurrent spatiotemporal-region))
         (not (= process process-boundary))
         (not (= process temporal-region))
         (not (= process zero-dimensional-temporal-region))
         (not (= process temporal-instant))
         (not (= process one-dimensional-temporal-region))
         (not (= process temporal-interval))
         (not (= process history))
         (not (= process spatiotemporal-region))
         (not (= process-boundary temporal-region))
         (not (= process-boundary zero-dimensional-temporal-region))
         (not (= process-boundary temporal-instant))
         (not (= process-boundary one-dimensional-temporal-region))
         (not (= process-boundary temporal-interval))
         (not (= process-boundary history))
         (not (= process-boundary spatiotemporal-region))
         (not (= temporal-region zero-dimensional-temporal-region))
         (not (= temporal-region temporal-instant))
         (not (= temporal-region one-dimensional-temporal-region))
         (not (= temporal-region temporal-interval))
         (not (= temporal-region history))
         (not (= temporal-region spatiotemporal-region))
         (not (= zero-dimensional-temporal-region temporal-instant))
         (not (= zero-dimensional-temporal-region
                 one-dimensional-temporal-region))
         (not (= zero-dimensional-temporal-region temporal-interval))
         (not (= zero-dimensional-temporal-region history))
         (not (= zero-dimensional-temporal-region spatiotemporal-region))
         (not (= temporal-instant one-dimensional-temporal-region))
         (not (= temporal-instant temporal-interval))
         (not (= temporal-instant history))
         (not (= temporal-instant spatiotemporal-region))
         (not (= one-dimensional-temporal-region temporal-interval))
         (not (= one-dimensional-temporal-region history))
         (not (= one-dimensional-temporal-region spatiotemporal-region))
         (not (= temporal-interval history))
         (not (= temporal-interval spatiotemporal-region))
         (not (= history spatiotemporal-region))))


  (cl:comment "zero-dimensional-spatial-region, one-dimensional-spatial-region, two-dimensional-spatial-region, three-dimensional-spatial-region are mutually disjoint [luc-1]"
    (and
     (not
      (exists (x t)
       (and (instance-of x zero-dimensional-spatial-region t)
        (instance-of x one-dimensional-spatial-region t))))
     (not
      (exists (x t)
       (and (instance-of x zero-dimensional-spatial-region t)
        (instance-of x two-dimensional-spatial-region t))))
     (not
      (exists (x t)
       (and (instance-of x zero-dimensional-spatial-region t)
        (instance-of x three-dimensional-spatial-region t))))
     (not
      (exists (x t)
       (and (instance-of x one-dimensional-spatial-region t)
        (instance-of x two-dimensional-spatial-region t))))
     (not
      (exists (x t)
       (and (instance-of x one-dimensional-spatial-region t)
        (instance-of x three-dimensional-spatial-region t))))
     (not
      (exists (x t)
       (and (instance-of x two-dimensional-spatial-region t)
        (instance-of x three-dimensional-spatial-region t))))))

)))