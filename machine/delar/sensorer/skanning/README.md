# Skanning och referensmodeller för sidotornet

**Källa till sanning för Core-omgivningens uppmätta geometri**, inpassad i fräsramen 2026-11-09. Filerna är för stora för git (ca 50 MB; punktmolnet går inte att packa). De ligger på Adams dator i `~/dev/lowrider-data/skanning-2026-11-09/` och som zip i `~/dev/lowrider-data/sidotorn-ref-2026-11-09.zip`. **Endast en kopia finns:** lägg även zip-filen i en molnmapp eller som GitHub-släpp tills vidare.

| Fil | Innehåll |
| --- | --- |
| `scan_pts_plan.npy` | 1,5 miljoner punkter (mm, fräsramen, bordet plant), området runt Core, ca 730 × 610 × 390 mm |
| `R_befintlig_core.stl`, `R_kjol.stl`, `R_dammsko.stl`, `R_tool_mount_t.stl`, `R_tool_mount_b.stl` | Referensmodeller av befintliga delar i samma ram |
| `R_SPMS664_referens.stl` | Servots referenskropp |

Inpassningen (`R`, `T`) och uppmätt offerskivenivå står i [sensorunderlaget](../README.md). `SHA256SUMS` i den här mappen är kontrollsummorna; stämmer de inte är det fel data:

```sh
cd ~/dev/lowrider-data/skanning-2026-11-09 && shasum -a 256 -c ~/dev/lowrider/machine/delar/sensorer/skanning/SHA256SUMS
```

Används av `granska_sidotorn.py --ref ~/dev/lowrider-data/skanning-2026-11-09`.
