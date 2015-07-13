{
//    volVectorField uPrime = U;
//    volScalarField TPrime = T;

    volSymmTensorField R = turbulence->R();
    volVectorField q = -kappat * fvc::grad(T);
    volScalarField nuSGS = turbulence->nut();
    kSGS = turbulence->k();
    volScalarField epsilonSGS = turbulence->epsilon();


    // Compute the running time averages of the fields and then get the fluctuation.
    if (runTime.value() >= avgStartTime)
    {
        Umean = (Umean * avgTimeSum) + (runTime.deltaT().value() * U);
        Tmean = (Tmean * avgTimeSum) + (runTime.deltaT().value() * T);
        Rmean = (Rmean * avgTimeSum) + (runTime.deltaT().value() * R);
        qmean = (qmean * avgTimeSum) + (runTime.deltaT().value() * q);
        nuSGSmean = (nuSGSmean * avgTimeSum) + (runTime.deltaT().value() * nuSGS);
        kSGSmean = (kSGSmean * avgTimeSum) + (runTime.deltaT().value() * kSGS);
        epsilonSGSmean = (epsilonSGSmean * avgTimeSum) + (runTime.deltaT().value() * epsilonSGS);

        avgTimeSum += runTime.deltaT().value();
        Info << "avgTimeSum = " << avgTimeSum << endl;

        Umean = Umean / avgTimeSum;
        Tmean = Tmean / avgTimeSum;
        Rmean = Rmean / avgTimeSum;
        qmean = qmean / avgTimeSum;
        nuSGSmean = nuSGSmean / avgTimeSum;
        kSGSmean = kSGSmean / avgTimeSum;
        epsilonSGSmean = epsilonSGSmean / avgTimeSum;


        // update the fluctuating part
        Uprime = U - Umean;
        Tprime = T - Tmean;
    }

    // Compute the running time averages of the correlation fields.
    if (runTime.value() >= corrStartTime)
    {


        uuPrime2 = (uuPrime2 * corrTimeSum) + (runTime.deltaT().value() * Foam::sqr(Uprime));
        uTPrime2 = (uTPrime2 * corrTimeSum) + (runTime.deltaT().value() * Tprime * Uprime);
        TTPrime2 = (TTPrime2 * corrTimeSum) + (runTime.deltaT().value() * Foam::sqr(Tprime));

        corrTimeSum += runTime.deltaT().value();
        Info << "corrTimeSum = " << corrTimeSum << endl;

        uuPrime2 = uuPrime2 / corrTimeSum;
        uTPrime2 = uTPrime2 / corrTimeSum;
        TTPrime2 = TTPrime2 / corrTimeSum;

        // for loop are time consuming. Use vetoriel computing instead
        uRMS.component(0) = Foam::sqrt(uuPrime2.component(0));
        uRMS.component(1) = Foam::sqrt(uuPrime2.component(3));
        uRMS.component(2) = Foam::sqrt(uuPrime2.component(5));
        TRMS = Foam::sqrt(TTPrime2);

        kResolved = 0.5 * (uuPrime2.component(0) + uuPrime2.component(3) + uuPrime2.component(5));
    }
}
